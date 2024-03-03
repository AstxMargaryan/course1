from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name='first'),
    path('<int:course_id>/', views.detail, name='detail'),
    path('<int:course_id>/rate/', views.rate_course, name='rate_course'),
]
