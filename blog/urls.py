"""
URL configuration for blog_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

urlpatterns = [
    path('students/', views.get_all_students, name='get_all_students'),
    path('students/create/', views.create_student, name='create_student'),
    path('students/<int:pk>/', views.get_student_by_id, name='get_student_by_id'),
    path('students/<int:pk>/update/', views.update_student, name='update_student'),
    path('students/<int:pk>/delete/', views.delete_student, name='delete_student'),
]
