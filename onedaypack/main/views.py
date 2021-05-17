from django.shortcuts import render

from main.models import FastPoint


def index(request):
    points = FastPoint.objects.all()
    content = {
        'points': points,
    }
    return render(request, 'main/index.html', content)

