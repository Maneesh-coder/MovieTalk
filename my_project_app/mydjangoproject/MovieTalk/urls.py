"""
URL configuration for 'my django site' project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the 'include()' function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add-movie/',views.add_movie, name='add_movie'),
    path('edit-movie/<int:movie_id>/',views.edit_movie, name='edit_movie' ),
    path('delete-movie/<int:movie_id>/', views.delete_movie, name='delete_movie'),
    # path('movie-added/', views.movie_added, name='movie_added'),
    # path('movie_edited/', views.movie_edited, name='movie_edited'),

]
