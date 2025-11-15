from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),                       # homepage / shows featured & recent
    path('projects/', views.project_list, name='project_list'),# all projects page
    path('projects/<int:pk>/', views.project_detail, name='project_detail'), # single project
    path('categories/<int:pk>/', views.category_detail, name='category_detail'), # category page
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
