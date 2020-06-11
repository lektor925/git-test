from django.contrib import admin
from django.urls import path

from movies.views import MovieView, MainPageView, MainView, AboutView

urlpatterns = [
    path('', MainView.as_view()),
    path('about/', AboutView.as_view()),
    path('movies/', MainPageView.as_view()),
    path('movies/<str:movie_name>/', MovieView.as_view()),
    path('admin/', admin.site.urls),
]
