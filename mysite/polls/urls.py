from django.urls import path
from . import views
from polls.views import *
#from polls.views import Student_Mgmt as sm_view
from polls.views import Manage_Student as ms_view
from polls.views import Manage_Department as md_view
from polls.views import Manage_Course as mc_view
from polls.views import Manage_Faculty as mf_view
from polls.views import Manage_Course as mc_view
from polls.views import StudentTableHTML
from polls.views import CourseTableHTML 
from polls.views import StudentDetailView
from polls.views import AddStudentView
from polls.views import CourseListView_p
from polls.views import AddStudent
 
urlpatterns = [
    path("", views.index, name="index"),
    path('polls',views.verify_user, name="verify_user"),
    path('polls', views.update_user, name="update_user"),
    #path('polls' ,sm_view.as_view()),
    path('polls',ms_view.as_view()),
    path('polls',mf_view.as_view()),
    path('polls',mc_view.as_view()),
    path('polls',StudentTableHTML.as_view()),
    path('polls',CourseTableHTML.as_view()),
    path('polls',AddStudent.as_view()),

    #path('courses_p/', csrf_exempt(CourseListView_p.as_view()), name='courses_p'),
    #path('polls',StudentDetailView.as_view()),
    #path('polls',AddStudentView.as_view())
    


    
    
   # path('courses/', csrf_exempt(CourseListView.as_view())),
    #path('student/<int:student_id>/', csrf_exempt(StudentDetailView.as_view())),
    #path('student_add/', csrf_exempt(AddStudentView.as_view())),
]


"""
from django.urls import path
from . import views

urlpatterns = [
    # Path for landing page
    path('', views.landing_page, name='landing_page'),

    # Path to get courses
    path('get_courses/', views.get_courses, name='get_courses'),

    # Path to get student information
    path('student_information/', views.student_information, name='student_information'),

    # Path to add a student
    path('add_student/', views.add_student, name='add_student'),

    # Other management paths (add these if you have corresponding views)
    path('manage_student/', views.Manage_Student.as_view(), name="manage_student"),
    path('manage_department/', views.Manage_Department.as_view(), name="manage_department"),
    path('manage_course/', views.Manage_Course.as_view(), name="manage_course"),
    path('manage_faculty/', views.Manage_Faculty.as_view(), name="manage_faculty"),
    path('manage_semester/', views.Manage_Semester.as_view(), name="manage_semester"),
    path('manage_subject/', views.Manage_Subject.as_view(), name="manage_subject"),
    path('manage_enrollment/', views.Manage_Enrollment.as_view(), name="manage_enrollment"),
    path('manage_exam/', views.Manage_Exam.as_view(), name="manage_exam"),
    path('student_table_html/', views.StudentTableHTML.as_view(), name="student_table_html"),
    path('course_table_html/', views.CourseTableHTML.as_view(), name="course_table_html"),
    path('course_type/', views.Chan_View.as_view(), name='course_type'),
    path('student_type/', views.Chan_View.as_view(), name='student_type'),
]

"""
