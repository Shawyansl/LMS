from django.db import models
from courses.models import Course
from users.models import UserProfile
# Create your models here.

class Quiz(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField()
    course_id = models.ForeignKey(Course , on_delete= models.CASCADE)

class Question(models.Model):
    QUESTION_TYPES = [
        ('MC', 'Multiple Choice'), #chand gozine
        ('SA', 'Short Answer'), #tashrihi
    ]
    quiz_id = models.ForeignKey(Quiz, on_delete= models.CASCADE , related_name='questions')
    text_question = models.TextField()
    question_type = models.CharField(max_length=2 , choices=QUESTION_TYPES , default='MC')

class Choice(models.Model):
    question   = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text       = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

class Answer(models.Model):
    student_id = models.ForeignKey("users.UserProfile" , on_delete=models.CASCADE , related_name='answers')
    question_id = models.ForeignKey(Question , on_delete=models.CASCADE , related_name='answers')
    selected_choice = models.ForeignKey(Choice , on_delete=models.CASCADE , null=True, blank=True , related_name='+')
    text_answer = models.TextField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    class Meta():
        unique_together = ('student_id', 'question_id')
        ordering = ['-submitted_at']

    def is_correct(self):
        if self.question_id.question_type == 'MC' and self.selected_choice:
            return self.selected_choice.is_correct
        
        return None
    def __str__(self):
        return f"{self.student_id} - {self.question_id} - {self.selected_choice} - {self.text_answer}"