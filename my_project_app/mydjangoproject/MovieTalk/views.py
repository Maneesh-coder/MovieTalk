from django.shortcuts import render,redirect
from .models import Movie


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies':movies})


def add_movie(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        duration = request.POST['duration']
        genre = request.POST['genre']
        movie = Movie(title=title, description=description, duration=duration, genre=genre)
        movie.save()
        return redirect('index')
        # return redirect('movie_added')
    return render(request, 'add_movie.html')


def edit_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if request.method == 'POST':
        movie.title = request.POST['title']
        movie.description = request.POST['description']
        movie.duration = request.POST['duration']
        movie.genre = request.POST['genre']
        movie.save()

        return redirect('index')
        # return redirect(('movie_edited'))
    return render(request, 'edit_movie.html', {'movie':movie})


def delete_movie(request, movie_id):
    Movie.objects.get(id=movie_id).delete()
    return redirect('index')


# def movie_added(request):
#     return render(request, 'movie_added.html')
#
#
# def movie_edited(request):
#     return render(request, 'movie_edited.html')
