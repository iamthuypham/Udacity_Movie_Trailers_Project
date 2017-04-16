from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.

def movies_list(request):
    movies = Movie.objects.all()
    # output = ', '.join(str(m) for m in movies)
    # return HttpResponse(output)
    return render(request, 'movie_trailers/movies_list.html', {'movies':movies})
    # return render_to_response(fresh_tomatoes.open_movies_page(movies))
    
