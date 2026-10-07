from django.urls import path
from . import views
from .views import task_list, add_task, delete_task, edit_task, toggle_status



urlpatterns = [
    path("tasks/", task_list, name="task_list"),
    path("5.6", task_list, name="task_list"),
    path("tasks/add/",views.add_task, name="add_task"),
    path("tasks/<int:task_id>/delete/", views.delete_task, name="delete_task"),
    path("tasks/<int:task_id>/edit/",edit_task, name="edit_task"),
    path("tasks/<int:task_id>/toggle-status/", toggle_status, name="toggle_status"),

]

