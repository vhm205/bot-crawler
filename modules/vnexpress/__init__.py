from bs4 import BeautifulSoup
import os
import requests
import bot

url_scraper = os.environ['VNEXPRESS_URL_SCRAPING']


def crawl_stock():
    url_stock = '{vnexpress_url}/kinh-doanh/chung-khoan'.format(
        vnexpress_url=url_scraper)
    response = requests.get(url_stock)

    htmlParser = BeautifulSoup(response.text, 'html.parser')
    title_news = htmlParser.select('h2.title-news')
    max_articles = 5

    if len(title_news) > max_articles:
        title_news = title_news[:max_articles]

    for news in title_news:
        title = news.text
        link = news.find('a').get('href')
        bot.send_message(text=f'{title}\n({link})')


def run():
    crawl_stock()
