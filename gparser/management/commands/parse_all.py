import datetime

from bs4 import BeautifulSoup
import requests
from django.core.management.base import BaseCommand

from gparser.models import News



url_wcc = "https://wccftech.com/category/news/page/"
url_g_radar = "https://www.gamesradar.com/news/page/"
url_pc_gamer = "https://www.pcgamer.com/hardware/news/page/"
url_t_hardware = "https://www.tomshardware.com/news/page/"


headers = {
        "user-agent": ("(Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                       + "AppleWebKit/537.36 (KHTML, like Gecko)"
                       + "Chrome/109.0.0.0 Safari/537.36")
}


def wcc_tags(url_wcc, headers):
    '''wccftech parser'''

    for page in range(6):
        page += 1
        url1 = url_wcc + str(page)
        response = requests.get(url1, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            main = soup.select('div[class="col-md-6"]'
)
            for article in main:
                pic = article.find('img').get('src')
                link = article.find('a').get('href')
                title = article.find('a').text
                date = article.find('div', class_='post-timestamp relative-time').get('data-time')
                
                try:
                    news = News.objects.get(link=link)
                    news.pic = pic
                    news.link = link
                    news.title = title
                    news.date = date
                    news.save()
                except News.DoesNotExist:
                    news = News(
                        pic=pic,
                        link=link,
                        title=title,
                        date=date,
                    ).save()
                print(f'article {news}')



def g_radar_tags(url_g_radar, headers):
    '''gamesradar parser'''

    for page in range(9):
        page += 1
        url1 = url_g_radar + str(page)
        response = requests.get(url1, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            g_radar_body = soup.find_all('div', class_='listingResults news')

            for article in g_radar_body:
                page = 1

                for item in range(20):
                    page += 1
                    page_class = "listingResult small result{}".format(str(page))
                    titles_g = article.find('div', class_=f'{page_class}')
                    pics = titles_g.find('div', class_='image-remove-reflow-container landscape').find('source')
                    pic = pics.get('data-original-mos')
                    link = titles_g.find('a').get('href')
                    title = titles_g.get_text(strip=True, separator=' ')
                    times = titles_g.find('time', class_="no-wrap relative-date date-with-prefix")
                    date = times.get('datetime')[0:10]
                    try:
                        news = News.objects.get(link=link)
                        news.pic = pic
                        news.link = link
                        news.title = title
                        news.date = date
                        news.save()
                    except News.DoesNotExist:
                        news = News(
                            pic=pic,
                            link=link,
                            title=title,
                            date=date,
                        ).save()
                    print(f'article {news}')


def pcgamer_tags(url_pc_gamer, headers):
    '''pcgamer parser'''

    for page in range(3):
        page += 1
        url1 = url_pc_gamer+ str(page)
        response = requests.get(url1, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            pc_gamer_body = soup.find_all('div', class_='listingResults news')

            for article in pc_gamer_body:
                page = 1

                for item in range(10):
                    page+=1
                    page_class = 'listingResult small result{}'.format(str(page))
                    main = article.find(f'div', class_=f'{page_class}')
                    pic = main.find('figure', class_='article-lead-image-wrap').get('data-original')
                    link = main.find('a').get('href')
                    title = main.find('a').get('aria-label')
                    dates = main.find('time')
                    date = dates.get('datetime')[0:10]

                    try:
                        news = News.objects.get(link=link)
                        news.pic = pic
                        news.link = link
                        news.title = title
                        news.date = date
                        news.save()
                    except News.DoesNotExist:
                        news = News(
                            pic=pic,
                            link=link,
                            title=title,
                            date=date,
                        ).save()
                    print(f'article {news}')

def tomshardaware_tags(url_t_hardware, headers):
    '''tomshardware parser'''

    for page in range(3):
        page += 1
        url1 = url_t_hardware + str(page)
        response = requests.get(url1, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            toms_main = soup.find_all('div', class_='listingResults mixed')

            for article in toms_main:
                main = article.find('div', class_='listingResult small result1')
                pic = main.find('figure', class_='article-lead-image-wrap').get('data-original')
                link = main.find('a').get('href')
                title = main.find('a').get('aria-label')
                date = main.find('time').get('datetime')[0:10]
                
                try:
                    news = News.objects.get(link=link)
                    news.pic = pic
                    news.link = link
                    news.title = title
                    news.date = date
                    news.save()
                except News.DoesNotExist:
                    news = News(
                        pic=pic,
                        link=link,
                        title=title,
                        date=date,
                    ).save()
                print(f'article {news}')

                page = 2

                for item in range(19):
                    page += 1
                    page_class = 'listingResult small result{}'.format(str(page))
                    main = article.find('div', class_=f'{page_class}')
                    pic = main.find('figure', class_='article-lead-image-wrap').get('data-original')
                    link = main.find('a').get('href')
                    title = main.find('a').get('aria-label')
                    date = main.find('time').get('datetime')[0:10]
                    
                    try:
                        news = News.objects.get(link=link)
                        news.pic = pic
                        news.link = link
                        news.title = title
                        news.date = date
                        news.save()
                    except News.DoesNotExist:
                        news = News(
                            pic=pic,
                            link=link,
                            title=title,
                            date=date,
                        ).save()
                    print(f'article {news}')


class Command(BaseCommand):
    help = 'Just parse them all!'

    def handle(self, *args, **options):
        wcc_tags(url_wcc, headers)
        g_radar_tags(url_g_radar, headers)
        pcgamer_tags(url_pc_gamer, headers)
        tomshardaware_tags(url_t_hardware, headers)