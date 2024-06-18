from django.shortcuts import render
from django.http import Http404

from catalogue.models import Artist

# Create your views here.
def index(request):
    artists = Artist.objects.all()
    title = 'Liste des artistes'

    return render(request, 'artist/index.html', {
        'artists': artists,
        'title': title
    })

def show(request, artist_id):
    try:
        artist = Artist.objects.get(artist_id=artist_id)  # Corrige le champ de clé primaire ici si nécessaire
    except Artist.DoesNotExist:
        raise Http404('Artist inexistant')

    title = 'Fiche d\'un artiste'

    return render(request, 'artist/show.html', {
        'artist': artist,
        'title': title
    })
