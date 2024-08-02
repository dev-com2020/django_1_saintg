from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Movie


# def home(request):
#     return HttpResponse('<h1>Witam w apce</h1>')


def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'name': 'Sekurit',
                                         'searchTerm': searchTerm,
                                         'movies': movies})


def about(request):
    return HttpResponse('<h1>Witam na stronie o nas</h1>')


def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'detail.html', {'movie': movie})
