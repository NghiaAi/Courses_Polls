from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, mssv, password=None, **extra_fields):
        if not mssv:
            raise ValueError('The MSSV must be set')
        user = self.model(mssv=mssv, raw_password=password, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mssv, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(mssv, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    mssv = models.CharField(max_length=20, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/avatar.jpg')
    raw_password = models.CharField(max_length=128, null=True, blank=True)  # Thêm trường này
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()
    class Meta:
        permissions = [
            ("can_view_ratings", "Can view ratings"),
            ("can_add_ratings", "Can add ratings"),
            ("can_edit_ratings", "Can edit ratings"),
            ("can_add_courses", "Can add courses"),
            ("can_edit_courses", "Can edit courses"),
        ]
    USERNAME_FIELD = 'mssv'
    REQUIRED_FIELDS = ['email', 'name']
class Course(models.Model):
    ma_mon_hoc = models.CharField(max_length=20, unique=True)
    ten_mon_hoc = models.CharField(max_length=100)
    so_tin_chi = models.IntegerField()
    ten_giang_vien = models.CharField(max_length=100)
    so_luong_cmt = models.IntegerField(default=0)
    def __str__(self):
        return self.ten_mon_hoc

class Rating(models.Model):
    mssv = models.CharField(max_length=20)
    name = models.CharField(max_length=100, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='ratings')
    cau1 = models.IntegerField()
    cau2 = models.IntegerField()
    cau3 = models.IntegerField()
    cau4 = models.TextField()

    class Meta:
        unique_together = ('mssv', 'course')

    def __str__(self):
        return f"Rating - {self.mssv} - {self.name} - {self.course.ma_mon_hoc}"
