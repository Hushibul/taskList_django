from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:task_id>/', views.task_details, name = 'task_details'),
    path('create/', views.create_task, name='create_task',),
    path('create-task/', views.create_task_page, name='create_task_page'),
    path('edit/<int:task_id>', views.edit_task_page, name='edit_task_page'),
    path('update/<int:task_id>', views.update_task, name='update_task'),
    path('delete/<int:task_id>', views.delete_task, name='delete_task')
]