from django.db import models
from role.models import Role
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission
from training_program.models import TrainingProgram
from module_group.models import Module
from course.models import Course
from subject.models import Subject

class User(AbstractUser):
    date_joined = models.DateTimeField(auto_now_add=True)
    training_programs = models.ManyToManyField(TrainingProgram)  
    modules = models.ManyToManyField(Module, related_name='assigned_users', blank=True)

    groups = models.ManyToManyField(
        Group,
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
        related_name='custom_user_groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
        related_name='custom_user_permissions',
    )


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_code = models.CharField(max_length=20, unique=True, null=True, blank=True)
    enrolled_courses = models.ManyToManyField('course.Course', blank=True) 
    
    def __str__(self):
        return f"{self.user.username} - Student"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  
    student = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    profile_picture_url = models.URLField(max_length=10000, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    learning_style = models.CharField(max_length=50, blank=True, null=True)
    preferred_language = models.CharField(max_length=50, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    reset_code = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return f"{self.user.username if self.user else self.student.username} - {self.role.role_name if self.role else 'No Role'}"


    
# class UserCourseProgress(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     training_program = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     progress = models.FloatField(default=0.0)  # Tiến độ học tập
#     last_accessed = models.DateTimeField(auto_now=True)  # Thời gian người dùng truy cập gần nhất

#     class Meta:
#         unique_together = ('user', 'training_program', 'subject')  # Đảm bảo mỗi người dùng chỉ có một tiến độ cho mỗi môn học trong chương trình

#     def __str__(self):
#         return f"{self.user.username} - {self.training_program.name} - {self.subject.name}"


