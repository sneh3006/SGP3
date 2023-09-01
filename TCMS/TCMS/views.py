from django.shortcuts import render
from accounts.models import Student

def homepage(request):
    return render(request, 'TCMS/homepage.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'accounts/manage_students.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'TCMS/add_student.html', {'form': form})

def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_report')
    else:
        form = AttendanceForm()
    return render(request, 'TCMS/mark_attendance.html', {'form': form})

def attendance_report(request):
    # Logic to generate attendance report
    attendance_data = Attendance.objects.all()  # You should adjust this query to filter as needed
    return render(request, 'TCMS/attendance_report.html', {'attendance_data': attendance_data})
