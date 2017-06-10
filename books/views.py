from django.shortcuts import render
from .models import Publisher


def get_all_publishers(request):
    publishers = Publisher.objects.all()
    print(publishers[0].name)

    return render(
        request,
        'publishers.html',
        {'publishers': publishers}
    )
