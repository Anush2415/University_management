"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),  # Include app-level URLs
]



"""
from django.contrib import admin
from django.urls import include, path,re_path as url
from polls.views import verify_user
from polls.views import *
from django.views.decorators.csrf import csrf_exempt
#from polls.views import Student_Mgmt as sm_view
from polls.views import Manage_Student as ms_view
from polls.views import Manage_Faculty as mf_view
from polls.views import Manage_Course as mc_view
from polls.views import StudentTableHTML
from polls.views import CourseTableHTML

from polls.views import StudentDetailView
from polls.views import CourseListView_p
from polls.views import AddStudent
 
urlpatterns = [
  
    path('polls/', include("polls.urls")),
    path('get_api/', verify_user, name='verify_user'),
    path('post_api/', update_user, name='update_user'), 
    path('admin/', admin.site.urls), 
    #path('sm_view/',csrf_exempt(sm_view.as_view())),
    path('ms_view/',csrf_exempt(ms_view.as_view())),
    path('mf_view/',csrf_exempt(mf_view.as_view())),
    path('mc_view/',csrf_exempt(mc_view.as_view())),
    path('student_list/',csrf_exempt(StudentTableHTML.as_view())),
    path('course_list/',csrf_exempt(CourseTableHTML.as_view())),
    path('add_student/',csrf_exempt(AddStudent.as_view())),
    #path('polls/', include("polls.urls")),

    #path('student/<int:student_id>/', StudentDetailView.as_view()),
    #path('student/add/', AddStudentView.as_view()),
]

