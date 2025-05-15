from django.db import models
from django.utils import timezone
from users.models import UserProfile
# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=120)
    instructor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default = timezone.now)
    updated_at = models.DateTimeField(default= timezone.now)
    is_active = models.BooleanField(default= True)


class Lesson(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=120)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()
    video_id = models.BigIntegerField()
    is_active = models.BooleanField(default= True)