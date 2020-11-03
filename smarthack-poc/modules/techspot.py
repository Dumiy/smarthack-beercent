import requests
from bs4 import BeautifulSoup

url = "https://www.techradar.com/uk/news/best-phone/"
myPhones = {}
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'}
def tech_news_best_phones():
    phone_review_links = []
    for i in range(1, 16):
        page = requests.get(url + str(i), headers=headers)
        soup = BeautifulSoup(page.content, features="html.parser")

        article = soup.find('div', {"id": "article-body"})
        title_text = soup.find('span', {"class": "title__text"})
        phone_spec = article.find('p', {"class": "specs__container"}).text
        page_text = []
        for p in article.findAll('p'):
            if len(p.text) > 50:
                page_text.append(p.text)
        # print(phone_spec)
        for div in soup.findAll('p'):
            a_list = div.findAll('a')
            for a in a_list:
                link_review = a['href']
                if '/reviews/' in link_review:
                    phone_review_links.append(link_review)
        myPhones[title_text.text[3:]] = page_text
    search_link = []
    phone_review_links = set(phone_review_links)
    for link in phone_review_links:
        page = requests.get(link, headers=headers)
        soup = BeautifulSoup(page.content, features="html.parser")

        article = soup.find('div', {"id": "article-body"})
        title_phones = soup.find('h1', {"class": "review-title-medium"})
        if article:
            page_text = []
            for p in article.findAll('p'):
                if p:
                    page_text.append(p.text)
            for div in soup.findAll('p'):
                a_list = div.findAll('a')
                for a in a_list:
                    link_review = a['href']
            myPhones[title_phones] = page_text
            search_link.append(link_review)
    return (myPhones,search_link)