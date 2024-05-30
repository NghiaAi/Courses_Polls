from rest_framework import serializers
from .models import User,Course,Rating

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['mssv', 'name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['ma_mon_hoc', 'ten_mon_hoc', 'so_tin_chi', 'ten_giang_vien', 'so_luong_cmt']
class RatingSerializer(serializers.ModelSerializer):
    course = serializers.SlugRelatedField(slug_field='ma_mon_hoc', queryset=Course.objects.all())
    
    class Meta:
        model = Rating
        fields = ['mssv', 'course', 'cau1', 'cau2', 'cau3', 'cau4']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['ma_mon_hoc'] = instance.course.ma_mon_hoc
        return ret