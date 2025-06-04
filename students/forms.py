from django import forms
from .models import Student, Grade, Subject

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['code', 'title']  # ✅ Only these two fields
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'year_level']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'year_level': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['subject', 'activity', 'quiz', 'exam']
        widgets = {
            'subject': forms.Select(attrs={'class': 'form-select'}),
            'activity': forms.NumberInput(attrs={'class': 'form-control'}),
            'quiz': forms.NumberInput(attrs={'class': 'form-control'}),
            'exam': forms.NumberInput(attrs={'class': 'form-control'}),
        }