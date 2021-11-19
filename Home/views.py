from django.shortcuts import render
from .models import *
from .utils import paginateProjects, searchMusics

# Create your views here.
def Home(request):
    musics, search_query = searchMusics(request)
    custom_range, musics = paginateProjects(request, musics, 20)
    Categories = Category.objects.all()
    context = {'popular_rec': musics, 'search_query' : search_query,
     'custom_range' : custom_range, 'category' : Categories}
    return render(request, 'Home/home.html', context)



def singleMusic(request, pk):
    MusicObj = HomePageModel.objects.get(id=pk)
    newset_musics = HomePageModel.objects.all()
    context = {'music' : MusicObj, 'new_musics' : newset_musics}
    return render(request, 'Home/single-music.html', context)



def categoryPage(request, pk):
    CategoryObj = Category.objects.get(id=pk)
    MusicObj = HomePageModel.objects.all().filter(category=CategoryObj)
    context = {'cat' : CategoryObj, 'Musics' : MusicObj}
    return render(request, 'Home/category-page.html', context)