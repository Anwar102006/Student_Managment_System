from django.urls import path
from student_mngmnt_sysytem import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("task4/", views.dashboard, name="dashboard_task4"),
    path(
        "students/add/",
        views.add_student,
        name="add_student"
    ),
    path(
        "marks/add/",
        views.add_marks,
        name="add_marks"
    ),
]