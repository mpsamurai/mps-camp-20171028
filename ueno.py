import doctest
import re
import os
import bs4
from urllib.parse import urlencode
import requests
from collections import defaultdict



top_page_links = defaultdict(dict)
category_page_links = defaultdict(dict)

def get_category_page_url(url):

    top_url = requests.get(url)
    top_html = bs4.BeautifulSoup(top_url.text)
    header_list = top_html.select('li.pc-header-nav-parent')

    for h in header_list:
        link_text = h.select('a')[0].text
        link = h.select('a')[0]
        linked_url = link.get('href')
        # カテゴリー毎のurlをget_detail_urlへ
        get_detail_page_url(linked_url)
        top_page_links[link_text] = linked_url

def get_detail_page_url(cate_url):
    cate_urls = requests.get(cate_url)
    cate_html = bs4.BeautifulSoup(cate_urls.text)
    item_list = cate_html.select('section[class=items-box]')

    for i in item_list:
        item_text = [img["alt"] for img in i.select('a img[alt]')]
        items = i.select('a')[0]
        # 詳細ページ毎のurlを取得
        item_url = items.get('href')
        get_detailed_info(item_url)
        category_page_links[item_text[0]] = item_url


def get_detailed_info(detail_url):
    """以下詳細情報の取得へ"""
    pass

if __name__ == '__main__':
    url = 'https://www.mercari.com/jp/'
    get_category_page_url(url)
    print("top_page_links", top_page_links)
    print("category_page_links", category_page_links)