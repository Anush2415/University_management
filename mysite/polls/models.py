from django.db import models
from datetime import date

class Department(models.Model):
    department_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.department_id})"

class Course(models.Model):
    course_id = models.CharField(max_length=10, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=50)
    course_type = models.CharField(max_length=10)  # UG or PG

    def __str__(self):
        return f"{self.name} ({self.course_id})"

class Semester(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='semesters')
    semester_number = models.PositiveIntegerField()

    def __str__(self):
        return f"Semester {self.semester_number} for {self.course.name}"

class Faculty(models.Model):
    faculty_id = models.CharField(max_length=10, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='faculties')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    role = models.CharField(max_length=20)  # Assistant Professor, Visiting Faculty, or Professor

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"

class Subject(models.Model):
    subject_code = models.CharField(max_length=10, primary_key=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=50)
    min_marks = models.PositiveIntegerField()  # Minimum marks required to pass the subject

    def __str__(self):
        return f"{self.name} ({self.subject_code})"

class Student(models.Model):
    student_id = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, default='default@example.com')
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    semester = models.ForeignKey(Semester, null=True, on_delete=models.SET_NULL)
    enrollment_start_date = models.DateField(default=date.today)
    enrollment_end_date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()

    def __str__(self):
        return f"Enrollment of {self.student} in {self.course}"

class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()

    def __str__(self):
        return f"Exam of {self.subject.name} on {self.exam_date} for {self.student}"

