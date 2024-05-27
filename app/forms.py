from django import forms
from .models import User
class AvatarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avatar'].label = "Thay đổi ảnh đại diện"
        


from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['ma_mon_hoc', 'ten_mon_hoc', 'so_tin_chi', 'ten_giang_vien']

