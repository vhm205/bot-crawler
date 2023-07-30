from bs4 import BeautifulSoup
import requests
import bot

url = 'https://vnexpress.net/kinh-doanh/chung-khoan'
response = requests.get(url)
htmlParser = BeautifulSoup(response.text, 'html.parser')
title_news = htmlParser.select('h2.title-news')


def crawling_news_stock():
    for news in title_news:
        title = news.text
        link = news.find('a').get('href')
        print(title, link)
        # bot.send_message(text=f'{title}\n({link})')
        # print('Scheduling for reminder...')


if __name__ == '__main__':
    print('Scheduling for crawling...')
    crawling_news_stock()
