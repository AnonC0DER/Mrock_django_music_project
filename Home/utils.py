from django.db import models
from .models import HomePageModel, PlayList, Category
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateProjects(request, musics, results):
    page = request.GET.get('page')
    # results = results
    paginator = Paginator(musics, results)

    try:
        musics = paginator.page(page)

    except PageNotAnInteger:
        page = 1
        musics = paginator.page(page)
    
    except EmptyPage:
        page = paginator.num_pages
        musics = paginator.page(page)

    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, musics



def searchMusics(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    category = Category.objects.filter(
        name__icontains=search_query
    )

    musics = HomePageModel.objects.distinct().filter(
        Q(music_name__icontains=search_query)  |
        Q(album_name__icontains=search_query) |
        Q(artist__icontains=search_query) |
        Q(category__in=category)
    )
    
    return musics, search_query
