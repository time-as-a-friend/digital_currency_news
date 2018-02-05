# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import requests
from article import Article

import config
from spiders.spider import Spider

directory_name = 'ft_chinese'
homePageUrl = 'http://www.ftchinese.com/'


class FTChineseSpider(Spider):
    def run(self):
        super(FTChineseSpider, self).ensure_news_dir(directory_name)

        news_list = load_news()
        for news in news_list:
            title = str(news.string)
            href = homePageUrl + news['href']
            if any(keyword in title.lower() for keyword in config.keywords):
                new_article = Article(title, '', href)
                super(FTChineseSpider, self).write_news_to_file(new_article, title)


def load_news():
    home_page_data = requests.get(homePageUrl)
    home_page_html = BeautifulSoup(home_page_data.text, "html.parser")
    news_elements = home_page_html.find_all(class_="item-container")
    all_news_list = []
    for news_element in news_elements:
        news_list = news_element.find_all('a', href=True)
        all_news_list += news_list
    return all_news_list