from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import UserViewSet,CourseViewSet
from app import views
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
# urls.py
from django.conf.urls import handler403

handler403 = 'app.views.custom_403_view'

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'courses', CourseViewSet) 
urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('trang-chu/', views.trang_chu_view, name='trang_chu'),
    path('mon-hoc/', views.danh_sach_mon_hoc_view, name='danh_sach_mon_hoc'),
    path('danh-gia-mon-hoc/<int:ma_mon_hoc>/', views.danh_gia_mon_view, name='danh_gia_mon_hoc'),
    path('danh-gia/', views.danh_gia_view, name='danh_gia'),
    path('thong-ke/', views.thong_ke_view, name='thong_ke'),
    path('tai-khoan/', views.tai_khoan_view, name='tai_khoan'),
    path('logout/', views.logout_view, name='dang_nhap'),
    path('submit-rating/', views.submit_rating, name='submit_rating'),
    path('get_ratings_for_course', views.get_ratings_for_course, name='get_ratings_for_course'),
    path('change_password/', views.change_password, name='change_password'),
    path('search-courses/', views.search_courses, name='search_courses'),
    path('change-avatar/', views.change_avatar, name='change_avatar'),
    path('export-course-data/<str:ma_mon_hoc>/', views.export_course_data, name='export_course_data'),
    path('reset-password/', views.password_reset_request, name='password_reset'),
    path('my-ratings/', views.my_ratings_view, name='my_ratings'),
    path('edit-rating/<str:ma_mon_hoc>/', views.edit_rating_view, name='edit_rating'),
    path('add_course/', views.add_course, name='add_course'),
    # mac dinh django
    path('admin/', admin.site.urls),
    path('admin_vippro/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),  # Thêm dòng này
    path('api/token/', obtain_auth_token, name='api_token_auth'), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)