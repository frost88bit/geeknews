from bs4 import BeautifulSoup
import requests


def wcc_details(news, headers):
    '''wccftech article ditails parser'''
    response = requests.get(news.link, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1').text
        pic = soup.find('div', class_='post-cover wp-lightbox')
        main = soup.find_all('main', class_='container')
        all_paragraphs = soup.find_all('div', class_='post')
        title = str(title).translate({ord('['): None})
        title = title.translate({ord(']'): None})
        pic = str(pic).translate({ord('['): None})
        pic = pic.translate({ord(']'): None})
        all_paragraphs = str(all_paragraphs).translate({ord('['): None})
        all_paragraphs = all_paragraphs.translate({ord(']'): None})  
        return{'title':title, 'pic': pic, 'all_paragraphs':all_paragraphs}
        

def gamesradar_details(news, headers):
    '''gamesradar article ditails parser'''
    response = requests.get(news.link, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        main = soup.find_all('article')
        header = soup.find_all('h1')
        body = soup.find_all('section', 'content-wrapper')
        header = str(header).translate({ord('['): None})
        header = header.translate({ord(']'): None})
        body = str(body).translate({ord('['): None})
        body = body.translate({ord(']'): None})
        return{'header':header, 'body':body}


def pc_gamer_details(news, headers):
    '''pc_gamer article ditails parser'''
    response = requests.get(news.link, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        header = soup.find_all('h1')
        par = soup.find_all('p', class_='strapline')
        pic = soup.find('div', class_='hero-image-padding')
        article_body = soup.find_all('div', class_='text-copy bodyCopy auto')
        sum_=(str(header)+str(par)+str(pic)+str(article_body))
        sum_ = sum_.translate({ord('['): None})
        sum_ = sum_.translate({ord(']'): None})  
        return{'sum':sum_}


def t_hardware_details(news, headers):
    '''tom`s_hardware article ditails parser'''
    response = requests.get(news.link, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        header = soup.find_all('h1')
        par = soup.find('p', class_='strapline')
        pic = soup.find('div', class_='hero-image-padding')
        section = soup.find_all('div', class_="text-copy bodyCopy auto")
        sum_ = (str(header)+str(par)+str(pic)+str(section))
        sum_ = sum_.translate({ord('['): None})
        sum_ = sum_.translate({ord(']'): None})
        return{'sum':sum_}
 
    
def the_gamer_details(news, headers):
    '''the gamer article ditails parser'''
    response = requests.get(news.link, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        header = soup.find_all('h1')
        pic = soup.find('figure').find('picture').find('source').get('srcset')
        body = soup.find_all('section', id='article-body')
        sum_=(str(header)+str(body))
        sum_ = sum_.translate({ord('['): None})
        sum_ = sum_.translate({ord(']'): None})
        return{'pic':pic, 'sum':sum_}


def game_rant_details(news, headers):
    '''gamerant article ditails parser'''
    response = requests.get(news.link, headers=headers)
        
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        header = soup.find_all('h1')
        pic = soup.find('figure').find('picture').find('source').get('srcset')
        body = soup.find_all('section', id='article-body')
        sum_ =(str(header)+str(body))
        sum_ = sum_.translate({ord('['): None})
        sum_ = sum_.translate({ord(']'): None})
        return{'pic':pic, 'sum':sum_}


if __name__ == '__main__':
    pass
