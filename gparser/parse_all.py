from bs4 import BeautifulSoup
import requests
import pytz
from datetime import datetime, time
from django.core.management.base import BaseCommand
from threading import Thread
from gparser.models import News


url_wcc = "https://wccftech.com/category/news/page/"
url_g_radar = "https://www.gamesradar.com/news/page/"
url_pc_gamer = "https://www.pcgamer.com/hardware/news/page/"
url_t_hardware = "https://www.tomshardware.com/news/page/"
url_the_gamer = "https://www.thegamer.com/category/game-news/"
url_game_rant = 'https://gamerant.com/gaming/'
url_ign = 'https://www.ign.com/news'

headers = {
        "user-agent": ("(Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                       + "AppleWebKit/537.36 (KHTML, like Gecko)"
                       + "Chrome/109.0.0.0 Safari/537.36")
    }


def wcc_tags(url_wcc, headers):
    '''wccftech articles parser'''
    for page in range(3):
        page += 1
        url1 = url_wcc + str(page)
        response = requests.get(url1, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            main = soup.select('div[class="col-md-6"]')

            for article in main:
                try:
                    pic = article.find('img').get('src')
                except AttributeError:
                    pic = ''
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
                

def g_radar_tags(url_g_radar, headers):
    '''gamesradar articles parser'''
    for page in range(4):
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
                    date = times.get('datetime')

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
                    

def pcgamer_tags(url_pc_gamer, headers):
    '''pcgamer articles parser'''
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
                    date = dates.get('datetime')

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
                    

def tomshardaware_tags(url_t_hardware, headers):
    '''tomshardware articles parser'''
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
                date = main.find('time').get('datetime')
                
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
                
                page = 2

                for item in range(19):
                    page += 1
                    page_class = 'listingResult small result{}'.format(str(page))
                    main = article.find('div', class_=f'{page_class}')
                    pic = main.find('figure', class_='article-lead-image-wrap').get('data-original')
                    link = main.find('a').get('href')
                    title = main.find('a').get('aria-label')
                    date = main.find('time').get('datetime')
                    
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


def the_gamer_tags(url_the_gamer, headers):
    """ the gamer articles parser"""
    response0 = requests.get(url_the_gamer, headers=headers)

    if response0.status_code == 200:
        soup = BeautifulSoup(response0.text, 'html.parser')
        main = soup.find_all('div', 'display-card' + ' ' + 'article' + ' ' + 'small')

        for item in main:
            pic = item.find('source').get('srcset')
            link = item.find('a', class_='dc-img-link').get('href')
            title = item.find('h5', class_='display-card-title').text
            date = item.find('time', class_='display-card-date').get('datetime')
            link = 'https://www.thegamer.com/' + link

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
            

    for page in range(1,4):
        page += 1
        url1 = url_the_gamer+str(page)
        response = requests.get(url1, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            main = soup.find_all('div', 'display-card' + ' ' + 'article' + ' ' + 'small')

            for item in main:
                pic = item.find('source').get('srcset')
                link = item.find('a', class_='dc-img-link').get('href')
                title = item.find('h5', class_='display-card-title').text
                date = item.find('time', class_='display-card-date').get('datetime')
                link = 'https://www.thegamer.com/' + link

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


def the_game_rant_tags(url_game_rant, headers):
    """ the gamerant articles parser"""
    response0 = requests.get(url_game_rant, headers=headers)

    if response0.status_code == 200:
        soup = BeautifulSoup(response0.text, 'html.parser')
        main = soup.find_all('div', 'display-card' + ' ' + 'article' + ' ' + 'small')

        for item in main:
            pic = item.find('source').get('srcset')
            link = item.find('a', class_='dc-img-link').get('href')
            title = item.find('h5', class_='display-card-title').text
            date = item.find('time', class_='display-card-date').get('datetime')
            link = 'https://gamerant.com' + link
            
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


    for page in range(1,3):
        page += 1
        url1 = url_game_rant+str(page)
        response = requests.get(url1, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            main = soup.find_all('div', 'display-card' + ' ' + 'article' + ' ' + 'small')

            for item in main:
                pic = item.find('source').get('srcset')
                link = item.find('a', class_='dc-img-link').get('href')
                title = item.find('h5', class_='display-card-title').text
                date = item.find('time', class_='display-card-date').get('datetime')
                link = 'https://gamerant.com' + link

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


def done():
    print('Data was collected')


def main_funk():
    Thread(target=wcc_tags(url_wcc, headers)).start()
    Thread(target=g_radar_tags(url_g_radar, headers)).start()
    Thread(target=pcgamer_tags(url_pc_gamer, headers)).start()
    Thread(target=tomshardaware_tags(url_t_hardware, headers)).start()
    Thread(target=the_gamer_tags(url_the_gamer, headers)).start()
    Thread(target=the_game_rant_tags(url_game_rant, headers)).start()
    Thread(target=done).start()

if __name__ == '__main__':
    pass