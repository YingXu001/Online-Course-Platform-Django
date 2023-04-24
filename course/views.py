from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Course
from .forms import CourseForm
from .forms import CommentForm
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.hashers import check_password
from django.contrib import auth
from django.shortcuts import render, get_object_or_404
from .models import Course
from django.contrib.auth.decorators import login_required
# from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages


# Create your views here.
@csrf_exempt
def course_list(request):
    if request.method == 'GET':
        all_courses = Course.objects.all().order_by('-created_at')
        hot_courses = Course.objects.order_by('-click')[:5]

        sort = request.GET.get('sort', '')
        if sort == 'hot':
            all_courses = all_courses.order_by('-click')
        elif sort == 'difficulty':
            all_courses = all_courses.order_by('difficulty')
        elif sort == 'title':
            all_courses = all_courses.order_by('title')

        return render(request, 'course_list.html', {
            'all_courses': all_courses,
            'hot_courses': hot_courses,
            'sort': sort,
        })

    else:
        data = {'status': 'error', 'message': 'Invalid request method'}
        return JsonResponse(data)


@csrf_exempt
@login_required(login_url='user/login/')
def course_create(request):
    print("Course create view called")
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            print("Course saved:", course)
            messages.success(request, 'Successfully created the course!')
            return redirect('course:course_detail', course_id=course.id)
        else:
            print("Form is not valid")  # Add this line
            print("Form errors:", form.errors)  # Add this line
    else:
        form = CourseForm()

    return render(request, 'course_create.html', {'form': form})

@csrf_exempt
def course_detail(request, course_id):
    if request.method == 'GET':
        course = get_object_or_404(Course, pk=course_id)
        course.click += 1
        course.save()
        return render(request, 'course_detail.html', {
            'course': course,
        })

    else:
        data = {'status': 'error', 'message': 'Invalid request method'}
        return JsonResponse(data)

def add_comment(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment_text = form.cleaned_data['comment']
            course.comment = comment_text
            course.save()
            return redirect('course:course_detail', course_id=course.id)
    else:
        form = CommentForm()

    context = {
        'course': course,
        'form': form,
    }

    return render(request, 'add_comment.html', context)

def delete_comment(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.comment = ""
        course.save()
        return redirect('course:course_detail', course_id=course.id)
    return render(request, 'delete_comment.html', {'course': course})

def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('course:course_list')
    return render(request, 'delete_course.html', {'course': course})
