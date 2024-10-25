from django.urls import path, include
from Task import views
urlpatterns = [
    path('add/', views.add_task, name="addtask"),
    path('edit/<int:id>', views.edit_task, name="edittask"),
    path('delete/<int:id>', views.delete_task, name="deletetask"),
]