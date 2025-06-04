from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    year_level = models.IntegerField()

    def __str__(self):
        return self.name

class Subject(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code} - {self.title}"

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades')
    
    activity = models.FloatField()
    quiz = models.FloatField()
    exam = models.FloatField()

    class Meta:
        unique_together = ('student', 'subject')
