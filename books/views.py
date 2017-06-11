from django.shortcuts import render
from .models import Publisher
from django.http import HttpResponse
from books.models import Book


def get_all_publishers(request):
    publishers = Publisher.objects.all()
    print(publishers[0].name)

    return render(
        request,
        'publishers.html',
        {'publishers': publishers}
    )

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(
            request,
            'search_results.html',
            {'books': books, 'query': q}
        )
    else:
        return HttpResponse('Search is empty')