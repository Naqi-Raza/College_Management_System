from django.urls import path 
from . import views
urlpatterns = [
    path("",views.Home,name="home"),
    path("navbar",views.navbar,name="navbar"),
    path("login",views.login,name="login"),
    path("Admission_form",views.Admission_form,name="Admission_form"),
    path("Submit_admission_form",views.Submit_admission_form,name="Submit_admission_form"),
    path("show_department",views.show_department,name="show_department"),
    path("show_fsc_eng",views.show_fsc_eng,name="show_fsc_eng"),
    path("show_ics",views.show_ics,name="show_ics"),
    path("show_fsc_med",views.show_fsc_med,name="show_fsc_med"),
    path("show_i_com",views.show_i_com,name="show_i_com"),
    path("show_Arts",views.show_Arts,name="show_Arts"), 
    path("show_science",views.show_science,name="show_science"),
    path("show_student_dashboard",views.show_student_dashboard,name="show_student_dashboard"),
    path("get_ics_students",views.get_ics_students,name="get_ics_students"),
    path("get_ics_subjects/<int:id>",views.get_ics_subjects,name="get_ics_subjects"),# api for get ics subjects
    path("edit_student/<str:program>/<int:id>",views.edit_student,name="edit_student"),
    path("update_student/<int:id>",views.update_student,name="update_student"),
    path("login_view",views.login_view,name="login_view"),
    path("teaching_detail",views.teaching_detail,name="teaching_detail"),
    path("teacher_profile",views.teacher_profile,name="teacher_profile"),
    
]   
