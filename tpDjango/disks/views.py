from django.http import Http404
from django.shortcuts import render
from disks.models import Album, Track, Artist

from disks.forms import RechercheForm


def acceuil(request):
    allAlbums = Album.objects.all()
    return render(request, 'base.html', {'allAlbums': allAlbums})


def album(request, id):
    allAlbums = Album.objects.all()
    try:
        alb = Album.objects.get(id=id)
        tracks = Track.objects.filter(album=alb)
    except Album.DoesNotExist:
        raise Http404
    return render(request, 'disks/album.html', locals())


def recherche(request):
    form = RechercheForm(request.GET or None)
    if form.is_valid():
        query = form.cleaned_data['query']
    print(query)
    print(query=="Audioslave")
    allAlbums = Album.objects.filter(title__icontains=query)
    print(query)
    print('Audioslave'==query)
    print(allAlbums)
    return render(request, 'base.html', locals())
