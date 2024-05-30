from rest_framework import viewsets, permissions
from .models import User,Course,Rating
from .serializers import UserSerializer,CourseSerializer
from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .forms import CourseForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Course, Rating
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Course

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
def login_view(request):
    if request.method == 'POST':
        mssv = request.POST.get('mssv')
        password = request.POST.get('password')
        user = authenticate(request, username=mssv, password=password)

        if user is not None:
            login(request, user)
            return redirect('trang_chu')
        else:
            messages.error(request, 'MSSV hoặc mật khẩu không chính xác')
    return render(request, 'DangNhap.html')
def logout_view(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
def trang_chu_view(request):
    return render(request, 'TrangChu.html')

# View cho trang danh sách môn học
@login_required(login_url='login')
def danh_sach_mon_hoc_view(request):
    courses = Course.objects.all()  # Truy vấn tất cả môn học từ cơ sở dữ liệu
    return render(request, 'DanhSachMonHoc.html', {'courses': courses})
from django.shortcuts import render
from .models import Course
@login_required(login_url='login')
def danh_gia_view(request):
    courses = Course.objects.all()
    return render(request, 'DanhGia.html', {'courses': courses})

# View cho trang đánh giá
@login_required(login_url='login')
def danh_gia_mon_view(request, ma_mon_hoc):
    course = get_object_or_404(Course, ma_mon_hoc=ma_mon_hoc)
    # Kiểm tra xem người dùng đã đánh giá môn học này chưa
    if Rating.objects.filter(mssv=request.user.mssv, course=course).exists():
        return JsonResponse({'status': 'error', 'message': 'Bạn đã đánh giá rồi!'}, status=400)
    
    if request.method == 'POST':
        mssv = request.user.mssv
        name = request.user.name
        cau1 = request.POST.get('question1')
        cau2 = request.POST.get('question2')
        cau3 = request.POST.get('question3')
        cau4 = request.POST.get('comment')
        
        Rating.objects.create(
            mssv=mssv,
            name=name,
            course=course,
            cau1=cau1,
            cau2=cau2,
            cau3=cau3,
            cau4=cau4
        )

        course.so_luong_cmt += 1
        course.save()

        return JsonResponse({'status': 'success', 'message': 'Đánh giá đã được gửi thành công'})
    else:
        return render(request, 'DanhGiaMon.html', {'course': course})

from django.shortcuts import get_object_or_404
@login_required(login_url='login')
def my_ratings_view(request):
    ratings = Rating.objects.filter(mssv=request.user.mssv).select_related('course')
    ratings_data = [
        {
            'ma_mon_hoc': rating.course.ma_mon_hoc,
            'ten_mon_hoc': rating.course.ten_mon_hoc,
            'so_tin_chi': rating.course.so_tin_chi,
            'ten_giang_vien': rating.course.ten_giang_vien,
        }
    for rating in ratings]
    return JsonResponse({'status': 'success', 'ratings': ratings_data})

@login_required(login_url='login')
def edit_rating_view(request, ma_mon_hoc):
    course = get_object_or_404(Course, ma_mon_hoc=ma_mon_hoc)
    rating = get_object_or_404(Rating, mssv=request.user.mssv, course=course)
    if request.method == 'POST':
        rating.cau1 = request.POST.get('question1')
        rating.cau2 = request.POST.get('question2')
        rating.cau3 = request.POST.get('question3')
        rating.cau4 = request.POST.get('comment')
        rating.save()
        return JsonResponse({'status': 'success', 'message': 'Đánh giá đã được cập nhật thành công'})
    return render(request, 'EditRating.html', {'rating': rating})
@login_required(login_url='login')
def thong_ke_view(request):
    ma_mon_hoc = request.GET.get('ma_mon_hoc', None)
    courses = Course.objects.all()
    selected_course = None
    ratings = None
    if ma_mon_hoc:
        selected_course = Course.objects.filter(ma_mon_hoc=ma_mon_hoc).first()
        if selected_course:
            ratings = selected_course.ratings.all()
    
    context = {
        'courses': courses,
        'selected_course': selected_course,
        'ratings': ratings if ratings else []
    }
    return render(request, 'ThongKe.html', context)


# View cho trang quản lý tài khoản người dùng
@login_required(login_url='login')
def tai_khoan_view(request):
    return render(request, 'TaiKhoan.html')

# View cho việc đăng xuất
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def submit_rating(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'success', 'message': 'Rating submitted successfully!'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
@login_required(login_url='login')
def get_ratings_for_course(request):
    ma_mon_hoc = request.GET.get('ma_mon_hoc')  # Lấy mã môn học từ truy vấn URL
    if ma_mon_hoc:
        ratings = Rating.objects.filter(ma_mon_hoc=ma_mon_hoc).values(
            'mssv', 'name', 'cau1', 'cau2', 'cau3', 'cau4'
        )
        return JsonResponse(list(ratings), safe=False)
    else:
        return JsonResponse({'error': 'Missing ma_mon_hoc parameter'}, status=400)


@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST['oldPassword']
        new_password = request.POST['newPassword']
        confirm_password = request.POST['confirmPassword']
        # Kiểm tra mật khẩu cũ có đúng không
        if not request.user.check_password(old_password):
            return JsonResponse({'status': 'error', 'message': 'Mật khẩu cũ không chính xác.'}, status=400)
        # Kiểm tra mật khẩu mới và xác nhận mật khẩu có khớp nhau không
        if new_password != confirm_password:
            return JsonResponse({'status': 'error', 'message': 'Mật khẩu mới và mật khẩu xác nhận không khớp.'}, status=400)
        # Thay đổi mật khẩu
        user = request.user
        user.set_password(new_password)
        user.raw_password = new_password 
        user.save()
        update_session_auth_hash(request, user)  # Để không đăng xuất người dùng sau khi thay đổi mật khẩu

        return JsonResponse({'status': 'success', 'message': 'Mật khẩu đã được đổi thành công!'}, status=200)
    else:
        # Hiển thị form thay đổi mật khẩu hoặc trả về một lỗi nếu không phải POST
        return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
def search_courses(request):
    if 'term' in request.GET:
        qs = Course.objects.filter(ten_mon_hoc__icontains=request.GET.get('term'))
        courses = list(qs.values('ma_mon_hoc', 'ten_mon_hoc'))
        # Thêm thông tin cho việc chuyển hướng sau này nếu cần
        for course in courses:
            course['url'] = f"/thong-ke/{course['ma_mon_hoc']}/"
        return JsonResponse(courses, safe=False)
    return JsonResponse([], safe=False)
from .forms import AvatarForm
from django.http import JsonResponse

@login_required(login_url='login')
def change_avatar(request):
    if request.method == 'POST' and request.FILES.get('avatar'):
        user = request.user
        user.avatar = request.FILES['avatar']
        user.save()
        return JsonResponse({'status': 'success', 'message': 'Avatar updated successfully!', 'avatar_url': user.avatar.url})
    return JsonResponse({'status': 'error', 'message': 'No file uploaded.'}, status=400)
@login_required(login_url='login')
def export_course_data(request, ma_mon_hoc):
    try:
        course = Course.objects.get(ma_mon_hoc=ma_mon_hoc)
        ratings = course.ratings.all()
    except Course.DoesNotExist:
        return HttpResponse("The specified course does not exist.", status=404)

    rating_values = {
        1: "Rất không hài lòng",
        2: "Không hài lòng",
        3: "Bình thường",
        4: "Hài lòng",
        5: "Rất hài lòng"
    }

    response_content = (
        f"Course Code: {course.ma_mon_hoc}\n"
        f"Course Name: {course.ten_mon_hoc}\n"
        f"Credits: {course.so_tin_chi}\n"
        f"Instructor: {course.ten_giang_vien}\n"
        f"Number of Comments: {course.so_luong_cmt}\n\n"
    )

    header = f"{'MSSV':<15} {'Name':<20} {'Question 1':<25} {'Question 2':<25} {'Question 3':<25} {'Question 4':<30}\n"
    response_content += header
    response_content += '-' * len(header) + '\n'

    for rating in ratings:
        cau1_text = rating_values.get(rating.cau1, "Không xác định")
        cau2_text = rating_values.get(rating.cau2, "Không xác định")
        cau3_text = rating_values.get(rating.cau3, "Không xác định")
        response_content += (
            f"{rating.mssv:<15} {rating.name:<20} {cau1_text:<25} {cau2_text:<25} {cau3_text:<25} {rating.cau4:<30}\n"
        )
    response = HttpResponse(response_content, content_type="text/plain")
    response['Content-Disposition'] = f'attachment; filename="{course.ten_mon_hoc}.txt"'
    return response
def password_reset_request(request):
    if request.method == "POST":
        mssv = request.POST.get('mssv')
        try:
            user = User.objects.get(mssv=mssv)
            send_mail(
                'Password Recovery',
                f'Your password is: {user.raw_password}',  
                'nta21303@gmail.com@gmail.com',
                [user.email],
                fail_silently=False,
            )
            messages.success(request, 'Mật khẩu đã được gửi đến email của bạn.')
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, 'MSSV không tồn tại.')
    return render(request, 'quenpass.html')

@login_required(login_url='login')
@permission_required('app.can_add_courses', raise_exception=True)
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mật khẩu đã được gửi đến email của bạn.')
            return redirect('trang_chu')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

def custom_403_view(request, exception):
    return render(request, '403.html', status=403)

def csrf_failure(request, reason=""):
    return render(request, '403.html', status=403)