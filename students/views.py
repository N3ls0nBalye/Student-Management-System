from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Student, Subject, Grade
from rest_framework import viewsets
from .models import Student, Subject, Grade
from .serializers import StudentSerializer, SubjectSerializer, GradeSerializer
from django.views.generic.edit import UpdateView
from .models import Student, Subject, Grade
from .serializers import StudentSerializer, SubjectSerializer, GradeSerializer
from django.views.decorators.http import require_POST
from .models import Subject
from .forms import SubjectForm, StudentForm, GradeForm

class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm  # or fields = ['code', 'title']
    template_name = 'students/subject_form.html'
    success_url = reverse_lazy('dashboard')

def dashboard(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'students/dashboard.html', {'students': students,
        'subjects': subjects,})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    grades = Grade.objects.filter(student=student)
    return render(request, 'students/student_detail.html', {'student': student, 'grades': grades})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student_detail', student.id)
    else:
        form = StudentForm()
    return render(request, 'student_add.html', {'form': form})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'students/student_form.html', {'form': form})

def grade_add(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.student = student
            grade.save()
            return redirect('student_detail', pk=student.id)
    else:
        form = GradeForm()
    return render(request, 'students/grade_form.html', {'form': form, 'student': student})

def grade_edit(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=grade.student.id)
    else:
        form = GradeForm(instance=grade)
    return render(request, 'students/grade_form.html', {'form': form, 'student': grade.student})

def subject_add(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SubjectForm()
    return render(request, 'students/subject_form.html', {'form': form})


def subject_add(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Or wherever you want
    else:
        form = SubjectForm()
    return render(request, 'subject_form.html', {'form': form})
@require_POST
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('dashboard')

@require_POST
def grade_delete(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    student_id = grade.student.id
    grade.delete()
    return redirect('student_detail', pk=student_id)    
@require_POST
def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    return redirect('dashboard')

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer