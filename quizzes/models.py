from django.db import models
from courses.models import Course
# Create your models here.

class Quiz(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField()
    duration = models.IntegerField()
    course_id = models.ForeignKey(Course , on_delete= models.CASCADE)

class Question(models.Model):
    quiz_id = models.ForeignKey(Quiz, on_delete= models.CASCADE)
    text = models.TextField()
    question_type = models.CharField(max_length=20)

class Answer(models.Model):
    student_id = models.BigIntegerField()
    question_id = models.ForeignKey(Question , on_delete=models.CASCADE)
    response = models.TextField()
    is_correct = models.BooleanField(default=False)
    submitted_at = models.DateTimeField()
