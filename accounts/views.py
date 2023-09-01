from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def login_view(request):
    if request.method == 'POST':
        # Handle login form submission here
        pass
    return render(request, 'accounts/login.html')

@login_required
def dashboard(request):
    # Add dashboard logic here
    pass



def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:student_list')
    else:
        form = StudentForm()
    return render(request, 'accounts/add_student.html', {'form': form})

def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('accounts:student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'accounts/update_student.html', {'form': form})

def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('accounts:student_list')
    return render(request, 'accounts/delete_student.html', {'student': student})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'accounts/student_list.html', {'students': students})



def manage_students(request):
    student_form = StudentForm(request.POST or None)
    students = Student.objects.all()

    if request.method == 'POST':
        if student_form.is_valid():
            student_form.save()
            return redirect('accounts:manage_students')

    context = {
        'student_form': student_form,
        'students': students,
    }
    return render(request, 'accounts/manage_students.html', context)

