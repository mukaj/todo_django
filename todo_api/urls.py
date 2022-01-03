from django.urls import path
from todo_api import views

urlpatterns = [
    path('tasks/', views.task_list),
    path('task/<int:pk>', views.task_detail),
]