from django.http import Http404, HttpResponse
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'new_view.html', {'name': 'world'})

def hours_ahead(request, offset, another):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hour(s), it will be %s. Extra argument is %s" % (offset, dt, another)
    return HttpResponse(html)

def render_users(request):
    return render(request, 'users.html', {'name': 'Looney'})