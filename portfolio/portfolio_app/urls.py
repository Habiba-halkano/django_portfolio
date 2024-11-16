from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/' , views.contact_form, name='contact'),
    path('success/', views.success, name='success'),
    path('projects/', views.projects, name='projects'),
]