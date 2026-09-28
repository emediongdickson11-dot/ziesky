from django.db import models

class Feedback(models.Model):
    student_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.student_name
    
