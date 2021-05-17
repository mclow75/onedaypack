from django.shortcuts import render

from main.models import FastPoint


def index(request):
    points = FastPoint.objects.all()
    context = {
        'points': points,
    }
    return render(request, 'main/index.html', context)

