from django.views.generic import ListView
from django.http import HttpResponse
from gparser.models import News
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from.parse_all import main_funk


from.helpers import (wcc_details,
                      gamesradar_details,
                      pc_gamer_details,
                      t_hardware_details,
                      the_gamer_details,
                      game_rant_details,
                      )

main_funk()

def index(request):
    """main page render"""
    news = News.objects.all()
    paginator = Paginator(news, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "gparser": News.objects.all().order_by('-date'),
        "page_obj": page_obj    
    }
    return render(request, "gparser/news.html", context=context)


def details(request, news_id):
    """article details render"""
    headers = {
        "user-agent": ("(Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                       + "AppleWebKit/537.36 (KHTML, like Gecko)"
                       + "Chrome/109.0.0.0 Safari/537.36")
        }
    
    news = get_object_or_404(News, id=news_id)

    if news.link.startswith('https://wccftech.com/'):
        result = wcc_details(news, headers)
        context = {
            'result':result
        }
        return render(request, 'gparser/wccft.html', context=context)
    
    elif news.link.startswith('https://www.gamesradar.com/'):
        result = gamesradar_details(news, headers)
        context = {
            'result':result
        }
        return render(request, 'gparser/gradar.html', context=context)
    
    elif news.link.startswith('https://www.pcgamer.com/'):
        result = pc_gamer_details(news, headers)
        context = {
            'result':result
        }
        return render(request, 'gparser/pcgamer.html', context=context)

    elif news.link.startswith('https://www.tomshardware.com/'):
        result = t_hardware_details(news, headers)
        context = {
            'result':result
        }
        return render(request, 'gparser/tomshw.html', context=context)

    elif news.link.startswith('https://www.thegamer.com/'):
        result = the_gamer_details(news, headers)
        context = {
            'result':result
        }
        return render(request, 'gparser/thegamer.html', context=context)

    elif news.link.startswith('https://gamerant.com/'):
        result = game_rant_details(news, headers)
        context = {
            'result':result
        }
        return render(request, 'gparser/gamerant.html', context=context)
    
    
def search_news(request):
    """search render"""
    if request.method == "POST":
        searched = request.POST['searched']
        news = News.objects.filter(title__contains=searched)
        context={
            "searched":searched,
            "gparser":news, 
        }
        return render(request, 'gparser/search_news.html', context=context)
    else:
        return render(request, 'gparser/search_news.html', context=context)