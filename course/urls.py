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
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'course'

urlpatterns = [
    path('display/', views.course_list, name='course_list'),
    path('create/', views.course_create, name='course_create'),
    path('detail/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/add_comment/', views.add_comment, name='add_comment'),
    path('course/<int:course_id>/delete_comment/', views.delete_comment, name='delete_comment'),
    path('course/<int:course_id>/delete_course/', views.delete_course, name='delete_course'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)