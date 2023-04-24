from django.shortcuts import render
from django.db.models import Q
from course.models import Course


def home(request):
    context = {
        
    }
    return render(request, 'home.html', context)

def search_results(request):
    query = request.GET.get('query')
    results = Course.objects.filter(
        Q(title__icontains=query)
    )
    context = {'query': query, 'results': results}
    return render(request, 'search_results.html', context=context)

