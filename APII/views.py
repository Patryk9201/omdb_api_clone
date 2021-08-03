from APII.models import Movie
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import MovieSerializer

class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
