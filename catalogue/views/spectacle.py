# catalogue/views/spectacle.py
from django.shortcuts import render
from django.http import Http404
from catalogue.models import Spectacle

def index(request):
    spectacles = Spectacle.objects.all()
    title = 'Liste des spectacles'

    return render(request, 'spectacle/index.html', {
        'spectacles': spectacles,
        'title': title
    })

def show(request, spectacle_id):
    try:
        spectacle = Spectacle.objects.get(spectacle_id=spectacle_id)
    except Spectacle.DoesNotExist:
        raise Http404('Spectacle inexistant')

    title = "Fiche d'un spectacle"

    return render(request, 'spectacle/show.html', {
        'spectacle': spectacle,
        'title': title
    })
