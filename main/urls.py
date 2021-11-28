"""calendar_class URL Configuration

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
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
app_name = 'main'

urlpatterns = [
    #auth views
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    #home pages
    path('faculty_home/',views.faculty_home,name='faculty_home'),#faculty home page on login
    path('student_home/', views.student_home, name='student_home'),#student home page on login
    #join create url
    path('join_create/',views.join_create,name='join_create'),#faculty page to join or create class or batch
    path('create_batch/<str:batch_name>/', views.create_batch,name='create_batch'),#api to batch page for faculty
    path('join_batch/<str:batch_code>/',views.join_batch,name='join_batch'),#api for student or teacher to join batch
    path('create_class/<str:batch_code>/<str:class_name>/',views.create_class,name='create_classs'),#api for teacher to create class
    path('join_class_teacher/<str:class_code>/',views.join_class_teacher,name='join_class_teacher'),#api for teacher to join class
    path('join_class_batch_student/',views.join_class_batch_student,name='join_class_batch_student'),#student page to join class or batch
    path('join_class_student/<str:class_code>/', views.join_class_student,name='join_class_student'),#api for student to join class
    #calendar based interface urls
    path('view_schedule/',views.view_schedule,name='view_schedule' ),#view schedule page
    path('show_calendar_plan/',views.show_calendar_plan,name='show_calendar_plan'),#api which takes json input and return stress level wieight for days. responsible for calendar heat coding
    path('get_all_tasks_on_day/',views.get_all_tasks_on_day,name='get_all_tasks_on_day'),#all tasks for day api
    path('delete_task/<int:task_id>/', views.delete_task,name="delete_task"),#api
    #task addition page
    path('add_task_page/',views.add_task_page, name='add_task_page'),#page for teacher to add task
    path('add_task_form_handler/', views.add_task_form_handler,name='add_task_form_handler'),#form for teacher to add task. redirects to add task page
    path('add_tasks_event/<str:batch_code>/<int:year>/<int:month>/<int:day>/<int:weight>/',views.add_task_view,name='add_task_view'),#not currently in use, api to add tasks
    #list of all batches user belongs to
    path('batch_view/<int:batch_id>/',views.batch_view, name='batch_view'),#not in use 
    path('all_user_batches/', views.all_user_batches,name='all_user_batches'),#all bataches user is part of
    #list of all classes in batch
    path('all_batch_classes_table_page/<int:batch_id>/', views.all_batch_classes_table_page, name='all_batch_classes_table_page'),#all classes in a batch 
    path('batch_class_list/<str:batch_code>/',views.all_batch_classes,name='batch_class_list'),#api for all classes in a batch 
    path('anonymous_classes/', views.all_anonymous_classes,name='anonymous_classes'),#classes for which user does not join batch
    #view for a class
    path('all_class_tasks/<int:class_id>/',views.all_class_tasks,name='all_class_tasks'),#all tasks for a class
    path('all_classes_teacher/',views.all_classes_teacher, name='all_classes_teacher'),#all teachers for a class
    #views dealing with student task submissions
    path('view_student_submission/<int:submission_id>', views.view_student_submission,name='view_student_submission'),#not in use
    path('grade_view_submitted_task/<int:submission_id>/' , views.grade_view_submitted_task, name='grade_view_submitted_task'),#page to view student task submission. if post request on grade form button, faculty can grade also
    path('all_submissions_for_task/<int:task_id>/<int:show_all>/',views.all_submissions_for_task,name='all_submissions_for_task'),#if show all is 0 for teacher only latest submission by student shown else all student submission shown. Incase of student only personal submission shown
    path('student_submit_task/<int:task_id>/',views.student_task_submission_page,name='student_task_submission'),#form for student to submit task
    #profile page
    path('user_profile_page/<int:user_id>/', views.user_profile_page , name='user_profile_page'),#profile page
    
]