from django.shortcuts import render, get_object_or_404
from .models import Course
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.loader import select_template
# Create your views here.


def first(request):
    courses = Course.objects.all()
    return render(request, 'first.html', {'courses': courses})
   
def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'detail.html', {'course': course})
    
        
def rate_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    
    if request.method == 'POST':
        new_rating = float(request.POST['rating'])
        course.update(new_rating)

    return render(request, 'rate_course.html', {'course': course})


