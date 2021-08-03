from APII.views import MovieListView
from django.urls import path

app_name = 'own_api'

urlpatterns = [
    path('all_movies/', MovieListView.as_view())
]
