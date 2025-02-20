from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from polls.models import Student
from polls.models import Course
from polls.models import Faculty
from polls.models import Department
from polls.models import Subject
from polls.models import Semester
from polls.models import Exam
from polls.models import Enrollment
from django.core.serializers.json import DjangoJSONEncoder

@csrf_exempt

class CourseListView_p(View):
    def get(self, request):
        course_type = request.GET.get('type')
        if course_type == 'UG':
            courses = Course.objects.using('studentdb').filter(course_type='UG')
        else:
            courses = Course.objects.using('studentdb').filter(course_type='PG')
        course_list = list(courses.values('id', 'name'))
        return JsonResponse(course_list, safe=False)

class StudentDetailView(View):
    def get(self, request, student_id):
        try:
            student = Student.objects.using('studentdb').get(student_id=student_id)
            student_data = {
                'student_id': student.student_id,
                'first_name': student.first_name,
                'last_name': student.last_name,
                'email_id': student.email_id,
                'department': {
                    'id': student.department.id,
                    'name': student.department.name
                },
                'course_id': {
                    'id': student.course_id.id,
                    'name': student.course_id.name
                },
                'semester': {
                    'semester_number': student.semester.semester_number
                },
                'enrollment_start_date': student.enrollment_start_date,
                'enrollment_end_date': student.enrollment_end_date
            }
            return JsonResponse(student_data)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)


class AddStudentView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            student = Student.objects.create(
                student_id=data['student_id'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                email_id=data['email_id'],
                department_id=data['department'],
                course_id=data['course_id'],
                semester_id=data['semester'],
                enrollment_start_date=data['enrollment_start_date'],
                enrollment_end_date=data['enrollment_end_date']
            )
            return JsonResponse({'success': True})
        except KeyError as e:
            return JsonResponse({'error': f'Missing field: {str(e)}'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

class AddStudent(View):
    def post(self, request):
        try:
            data = json.loads(request.body.decode("utf-8"))

            # Check if data is a dictionary and contains the necessary fields
            if isinstance(data, dict):
                Student.objects.using('studentdb').create(
                    student_id=data.get('student_id'),
                    first_name=data.get('first_name'),
                    last_name=data.get('last_name'),
                    email=data.get('email'),
                    department_id=data.get('department_id'),
                    course_id=data.get('course_id'),
                )
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Expected a dictionary with student details'})
        
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})


class StudentTableHTML(View):
    def get(self, request):
        studentid = request.GET.get('student_id','')
        students = Student.objects.using('studentdb').filter(student_id=studentid).values(
            'student_id', 'first_name', 'last_name', 'email',
            'department_id', 'course_id', 'semester_id',
            'enrollment_start_date', 'enrollment_end_date'
        )
        return JsonResponse(list(students), safe=False)
class CourseTableHTML(View):
    def get(self, request):
        course_type = request.GET.get('type','')
        if course_type == 'UG':
            courses = Course.objects.using('studentdb').filter(course_type='UG')
        else:
            courses = Course.objects.using('studentdb').filter(course_type='PG')
        course_list = list(courses.values('course_id','department_id', 'name'))
        return JsonResponse(course_list, safe=False)
    
"""def get(self,request):
        courses = Course.objects.using('studentdb').all().values(
            'course_id','department_id','name','course_type')
        return JsonResponse(list(courses), safe=False)"""


def index(request):
	return HttpResponse("Hello Student")
def verify_user(request):
	userid=request.GET.get('Userid','')
	resp={}
	if userid:
		resp['status'] = 'success'
	return HttpResponse(json.dumps(resp),content_type='application/json')

def update_user(request):
	userid=request.POST.get('Userid','')
	resp=[]
	if userid:
		resp['status']='Success'
		resp['status.code']=200
	else:
		resp['status'] = 'Failed'
		resp['status code']=200
	return HttpResponse(json.dumps(resp), content_type='application/json')
"""class Student_Mgmt(View): #This 
	def get(self, request):
		userid = request.GET.get('userid','')
		resp = {}
		if userid:
			resp['status'] = 'Success'
			resp['status_code'] = '200'
		return HttpResponse(json.dumps(resp), content_type = 'application/json')
	def post(self, request):
		user_name=json.loads(request.body)
		resp={}
		if user_name: 
            resp['status']='Success'
		   # resp['status_code']='200'
		   # resp['data']=user_name[0]['user_name']
        return HttpResponse(json.dumps(resp),content_type='application/json')"""


def success_200():
    resp={}
    resp['status'] = 'Success'
    resp['status_code'] = '200'
    return resp
def error_404(string):
    resp={}
    resp['status'] = 'Failed'
    resp['status_code'] = '404'
    resp['error'] = string
    return resp
    
def error_400_e(e):
    resp={}
    resp['status'] = 'Failed'
    resp['status_code'] = '400'
    resp['error'] = str(e)
    return resp 
		
class Manage_Student(View):
    def post(self, request):
        resp={}
        para_data=json.loads(request.body)
        action_code=para_data[0]['action_code']
        first_name=para_data[0]['first_name']
        last_name_1=para_data[0]['last_name']
        student_id_1=para_data[0]['student_id']
        course_id_id=para_data[0]['course_id']
        email_id=para_data[0]['email_id']
        department_id1=para_data[0]['department_id']
        
        if action_code == 'I':
            result = Student.objects.using('studentdb').filter(student_id=student_id_1).values()
            if result.exists():
                resp=error_404(f'" student_id:{student_id_1}"   alredy  exists')
                return HttpResponse(json.dumps(resp,cls=DjangoJSONEncoder),content_type='application/json')
            try:
                data = Student(first_name=first_name,last_name=last_name_1,email=email_id,student_id=student_id_1,course_id=course_id_id,department_id=department_id1)
                data.save(using='studentdb')                
                resp=success_200()                
            except Exception as e:
                resp=error_400_e(e)
            return HttpResponse(json.dumps(resp),content_type='application/json')
            
        elif action_code == 'U':
            try:
                data = Student.objects.using('studentdb').filter(
                    student_id=student_id_1
                ).update(email=email_id,department_id=department_id1,course_id=course_id_id)
                if data > 0:
                    resp=success_200()
                else:
                    resp=error_404('Student not found')
            except Exception as e:
                resp=error_400_e(e)

        elif action_code == 'D':
            try:
                data = Student.objects.using('studentdb').filter(
                    student_id=student_id_1
                ).delete()
                if data[0] > 0:
                    resp=success_200()
                else:
                    resp=error_404('Student not found')
            except Exception as e:
                resp=error_400_e(e)
        

        else:
            resp=error_404('Invalid action code')

        return HttpResponse(json.dumps(resp, cls=DjangoJSONEncoder), content_type='application/json')

        

    def get(self, request):
        try:
            result = Student.objects.using('studentdb').filter(student_id=request.GET.get("student_id", '')).values()
            if result.exists():
                return HttpResponse(json.dumps(list(result), cls=DjangoJSONEncoder), content_type='application/json')
            else:
                resp=error_404('Student not found')
                return HttpResponse(json.dumps(resp), content_type='application/json')
        except Exception as e:
            resp =error_400_e(e)
            return HttpResponse(json.dumps(resp), content_type='application/json')


# for manageing department
class Manage_Department(View):
    def post(self, request):
        resp = {}
        para_data = json.loads(request.body)
        action_code = para_data[0]['action_code']
        department_id1 = para_data[0]['department_id']
        name1 = para_data[0]['name']

        if action_code == 'I':
            result = Department.objects.using('studentdb').filter(department_id=department_id1).values()
            if result.exists():
                resp=error_404(f'" department_id : {department_id1}"   alredy  exists')
                return HttpResponse(json.dumps(resp,cls=DjangoJSONEncoder),content_type='application/json')
            try:
                data = Department(department_id=department_id1, name=name1)
                data.save(using='studentdb')
                resp=success_200()
            except Exception as e:
                resp=error_400_e(e)
        elif action_code == 'U':
            try:
                data = Department.objects.using('studentdb').filter(department_id=department_id1).update(name=name1)
                if data > 0:
                   resp=success_200() 
                else:
                    resp=error_404('Department not found')
            except Exception as e:
                resp=error_400_e(e)
        elif action_code == 'D':
            try:
                data = Department.objects.using('studentdb').filter(department_id=department_id1).delete()
                if data[0] > 0:
                    resp=success_200()
                else:
                    resp=error_404('Department not found')
            except Exception as e:
                resp=error_400_e(e)
        else:
            resp=error_404('Invalid action code')

        return HttpResponse(json.dumps(resp, cls=DjangoJSONEncoder), content_type='application/json')

    def get(self, request):
        try:
            result = Department.objects.using('studentdb').filter(department_id=request.GET.get("department_id", '')).values()
            if result.exists():
                return HttpResponse(json.dumps(list(result), cls=DjangoJSONEncoder), content_type='application/json')
            else:
                resp=error_404('Department not found')
                return HttpResponse(json.dumps(resp), content_type='application/json')
        except Exception as e:
            resp=error_400_e(e)
            return HttpResponse(json.dumps(resp), content_type='application/json')

# for Course managment

class Manage_Course(View):
    def post(self, request):
        resp = {}
        para_data = json.loads(request.body)
        action_code = para_data[0]['action_code']
        course_id1 = para_data[0]['course_id']
        department_id1 = para_data[0]['department_id']
        name1 = para_data[0]['name']
        course_type1 = para_data[0]['course_type']
        
        if action_code == 'I':
            result = Course.objects.using('studentdb').filter(course_id=course_id1).values()
            if result.exists():
                resp=error_404(f'" course_id : {course_id1}"   alredy  exists')
                return HttpResponse(json.dumps(resp,cls=DjangoJSONEncoder),content_type='application/json')
            try:
                #department = Department.objects.get(department_id=department_id1)
                data = Course(course_id=course_id1, department_id=department_id1, name=name1, course_type=course_type1)
                data.save(using='studentdb')
                resp=success_200()
            except Exception as e:
                resp=error_400_e(e)
        elif action_code == 'U':
            try:
                data = Course.objects.using('studentdb').filter(course_id=course_id1).update(name=name1, course_type=course_type1)
                if data > 0:
                    resp=success_200()
                else:
                    resp=error_404('Course not found')
            except Exception as e:
                resp=error_400_e(e)
        elif action_code == 'D':
            try:
                data = Course.objects.using('studentdb').filter(course_id=course_id1).delete()
                if data[0] > 0:
                    resp=success_200()
                else:
                    resp=error_404('Course not found')
            except Exception as e:
                resp=error_400_e(e)
        else:
            resp=error_404('Invalid action code')

        return HttpResponse(json.dumps(resp, cls=DjangoJSONEncoder), content_type='application/json')

    def get(self, request):
        try:
            result = Course.objects.using('studentdb').filter(course_id=request.GET.get("course_id", '')).values()
            if result.exists():
                return HttpResponse(json.dumps(list(result), cls=DjangoJSONEncoder), content_type='application/json')
            else:
                resp=error_404('Course not found')
                return HttpResponse(json.dumps(resp), content_type='application/json')
        except Exception as e:
            resp=error_400_e(e)
            return HttpResponse(json.dumps(resp), content_type='application/json')

# for managing faculty

class Manage_Faculty(View):
    def post(self, request):
        resp = {}
        para_data = json.loads(request.body)
        action_code = para_data[0]['action_code']
        faculty_id1 = para_data[0]['faculty_id']
        department_id1 = para_data[0]['department_id']
        first_name1 = para_data[0]['first_name']
        last_name1 = para_data[0]['last_name']
        email1 = para_data[0]['email']
        role1 = para_data[0]['role']

        if action_code == 'I':
            result = Faculty.objects.using('studentdb').filter(faculty_id=faculty_id1).values()
            if result.exists():
                resp=error_404(f'" faculty_id : {faculty_id1}"   alredy  exists')
                return HttpResponse(json.dumps(resp,cls=DjangoJSONEncoder),content_type='application/json')                    
            try:
                #department = Department.objects.get(department_id=department_id1)
                data = Faculty(faculty_id=faculty_id1, department_id=department_id1, first_name=first_name1, last_name=last_name1, email=email1, role=role1)
                data.save(using='studentdb')
                resp=success_200()
            except Exception as e:
                resp=error_400_e(e)
        elif action_code == 'U':
            try:
                data = Faculty.objects.using('studentdb').filter(faculty_id=faculty_id1).update(
                    department=department_id1, first_name=first_name1, last_name=last_name1, email=email1, role=role1
                )
                if data > 0:
                    resp=success_200()
                else:
                    resp=error_404('Faculty not found')
            except Exception as e:
                resp=error_400_e(e)
        elif action_code == 'D':
            try:
                data = Faculty.objects.using('studentdb').filter(faculty_id=faculty_id1).delete()
                if data[0] > 0:
                    resp=success_200()
                else:
                    resp=error_404('Faculty not found')
            except Exception as e:
                resp=error_400_e(e)
        else:
            resp=error_404('Invalid action code')

        return HttpResponse(json.dumps(resp, cls=DjangoJSONEncoder), content_type='application/json')

    def get(self, request):
        try:
            result = Faculty.objects.using('studentdb').filter(faculty_id=request.GET.get("faculty_id", '')).values()
            if result.exists():
                return HttpResponse(json.dumps(list(result), cls=DjangoJSONEncoder), content_type='application/json')
            else:
                resp=error_404('Faculty not found')
                return HttpResponse(json.dumps(resp), content_type='application/json')
        except Exception as e:
            resp=error_400_e(e)
            return HttpResponse(json.dumps(resp), content_type='application/json')

# for managing semester

class Manage_Semester(View):
    def post(self, request):
        resp = {}
        para_data = json.loads(request.body)
        action_code = para_data[0]['action_code']
        course_id1 = para_data[0]['course_id']
        semester_number1 = para_data[0]['semester_number']

        if action_code == 'I':
            result = Semester.objects.using('studentdb').filter(semester_number=semester_number1,course_id=course_id1).values()
            if result.exists():
                resp=error_404(f'" semester_number : {semester_number1}"   alredy  exists')
                return HttpResponse(json.dumps(resp,cls=DjangoJSONEncoder),content_type='application/json')
            try:
                #course = Course.objects.get(course_id=course_id)
                data = Semester(course_id=course_id1, semester_number=semester_number1)
                data.save(using='studentdb')
                resp=success_200()
            except Exception as e:
                resp=error_400_e(e)
        elif action_code == 'U':
            try:
                data = Semester.objects.using('studentdb').filter(course_id=course_id1, semester_number=semester_number1).update(semester_number=semester_number1)
                if data > 0:
                    resp=success_200()
                else:
                    resp=error_404('Semester not found')
            except Exception as e:
                resp=error_400_e(e)
        elif action_code == 'D':
            try:
                data = Semester.objects.using('studentdb').filter(course_id=course_id1, semester_number=semester_number1).delete()
                if data[0] > 0:
                    resp=success_200()
                else:
                    resp=error_404('Semester not found')
            except Exception as e:
                resp=error_400_e(e)
        else:
            resp=error_404('Invalid action code')

        return HttpResponse(json.dumps(resp, cls=DjangoJSONEncoder), content_type='application/json')

    def get(self, request):
        try:
            result = Semester.objects.using('studentdb').filter(course_id=request.GET.get("course_id", ''), semester_number=request.GET.get("semester_number", '')).values()
            if result.exists():
                return HttpResponse(json.dumps(list(result), cls=DjangoJSONEncoder), content_type='application/json')
            else:
                resp=error_404('Semester not found')
                return HttpResponse(json.dumps(resp), content_type='application/json')
        except Exception as e:
            resp=error_400_e(e)
            return HttpResponse(json.dumps(resp), content_type='application/json')

# managing subject

class Manage_Subject(View):
    def post(self, request):
        resp = {}
        para_data = json.loads(request.body)
        action_code = para_data[0]['action_code']
        subject_code1 = para_data[0]['subject_code']
        semester_id1 = para_data[0]['semester_id']
        name1 = para_data[0]['name']
        min_marks1 = para_data[0]['min_marks']

        if action_code == 'I':
            result = Subject.objects.using('studentdb').filter(subject_code=subject_code1).values()
            if result.exists():
                resp=error_404(f'" subject_code : {subject_code1}"   alredy  exists')
                return HttpResponse(json.dumps(resp,cls=DjangoJSONEncoder),content_type='application/json')
            try:
                #semester = Semester.objects.get(id=semester_id1)
                data = Subject(subject_code=subject_code1, semester=semester_id1, name=name1, min_marks=min_marks1)
                data.save(using='studentdb')
                resp=success_200()
            except Exception as e:
                resp=error_400_e(e)
        elif action_code == 'U':
            try:
                data = Subject.objects.using('studentdb').filter(subject_code=subject_code1).update(name=name1, min_marks=min_marks1)
                if data > 0:
                    resp=success_200()
                else:
                    resp=error_404('Subject not found')
            except Exception as e:
                resp=error_400_e(e)
        elif action_code == 'D':
            try:
                data = Subject.objects.using('studentdb').filter(subject_code=subject_code1).delete()
                if data[0] > 0:
                    resp=success_200()
                else:
                    resp=error_404('Subject not found')
            except Exception as e:
                resp=error_400_e(e)
        else:
            resp=error_404('Invalid action code')

        return HttpResponse(json.dumps(resp, cls=DjangoJSONEncoder), content_type='application/json')

    def get(self, request):
        try:
            result = Subject.objects.using('studentdb').filter(subject_code=request.GET.get("subject_code", '')).values()
            if result.exists():
                return HttpResponse(json.dumps(list(result), cls=DjangoJSONEncoder), content_type='application/json')
            else:
                resp=error_404('Subject not found')
                return HttpResponse(json.dumps(resp), content_type='application/json')
        except Exception as e:
            resp=error_400_e(e)
            return HttpResponse(json.dumps(resp), content_type='application/json')

#managing 

class Manage_Enrollment(View):
    def post(self, request):
        resp = {}
        para_data = json.loads(request.body)
        action_code = para_data[0]['action_code']
        student_id1 = para_data[0]['student_id']
        course_id1 = para_data[0]['course_id']
        enrollment_date1 = para_data[0]['enrollment_date']

        if action_code == 'I':
            try:
                #student = Student.objects.get(student_id=student_id)
                #course = Course.objects.get(course_id=course_id)
                data = Enrollment(student=student_id1, course=course_id1, enrollment_date=enrollment_date1)
                data.save(using='studentdb')
                resp=success_200()
            except Exception as e:
                resp=error_400_e(e)
        elif action_code == 'U':
            try:
                data = Enrollment.objects.using('studentdb').filter(student=student_id1, course=course_id1).update(enrollment_date=enrollment_date1)
                if data > 0:
                    resp=success_200()
                else:
                    resp=error_404('Enrollment not found')
            except Exception as e:
                resp=error_400_e(e)
        elif action_code == 'D':
            try:
                data = Enrollment.objects.using('studentdb').filter(student=student_id1, course=course_id1).delete()
                if data[0] > 0:
                    resp=success_200()
                else:
                    resp=error_404('Enrollment not found')
            except Exception as e:
                resp=error_400_e(e)
        else:
            resp=error_404('Invalid action code')

        return HttpResponse(json.dumps(resp, cls=DjangoJSONEncoder), content_type='application/json')

    def get(self, request):
        try:
            result = Enrollment.objects.using('studentdb').filter(student=request.GET.get("student_id", ''), course=request.GET.get("course_id", '')).values()
            if result.exists():
                return HttpResponse(json.dumps(list(result), cls=DjangoJSONEncoder), content_type='application/json')
            else:
                resp=error_404('Enrollment not found')
                return HttpResponse(json.dumps(resp), content_type='application/json')
        except Exception as e:
            resp=error_400_e(e)
            return HttpResponse(json.dumps(resp), content_type='application/json')

#managing for Exam

class Manage_Exam(View):
    def post(self, request):
        resp = {}
        para_data = json.loads(request.body)
        action_code = para_data[0]['action_code']
        subject_code1 = para_data[0]['subject_code']
        student_id1 = para_data[0]['student_id']
        exam_date1 = para_data[0]['exam_date']
        marks1 = para_data[0]['marks']

        if action_code == 'I':
            try:
                #subject = Subject.objects.get(subject_code=subject_code)
                #student = Student.objects.get(student_id=student_id)
                data = Exam(subject=subject_code1, exam_date=exam_date1, student=student_id1, marks=marks1)
                data.save(using='studentdb')
                resp=success_200()
            except Exception as e:
                resp=error_400_e(e)
        elif action_code == 'U':
            try:
                data = Exam.objects.using('studentdb').filter(subject=subject_code1, student=student_id1).update(exam_date=exam_date1, marks=marks1)
                if data > 0:
                    resp=success_200()
                else:
                    resp=error_404('Exam not found')
            except Exception as e:
                resp=error_400_e(e)
        elif action_code == 'D':
            try:
                data = Exam.objects.using('studentdb').filter(subject=subject_code1, student=student_id1).delete()
                if data[0] > 0:
                    resp=success_200()
                else:
                    resp=error_404('Exam not found')
            except Exception as e:
                resp=error_400_e(e)
        else:
            resp=error_404('Invalid action code')

        return HttpResponse(json.dumps(resp, cls=DjangoJSONEncoder), content_type='application/json')

    def get(self, request):
        try:
            result = Exam.objects.using('studentdb').filter(subject=request.GET.get("subject_code", ''), student=request.GET.get("student_id", '')).values()
            if result.exists():
                return HttpResponse(json.dumps(list(result), cls=DjangoJSONEncoder), content_type='application/json')
            else:
                resp=error_404('Exam not found')
                return HttpResponse(json.dumps(resp), content_type='application/json')
        except Exception as e:
            resp=error_400_e(e)
            return HttpResponse(json.dumps(resp), content_type='application/json')
