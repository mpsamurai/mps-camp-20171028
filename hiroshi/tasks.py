import time
from celery.decorators import task
import doctest
import re
import os
import bs4
from urllib.parse import urlencode
import requests
from collections import defaultdict


top_page_links = defaultdict(dict)
# child_page_links = []

@task
def get_top_page_links(url):

    resp = requests.get(url)
    html = bs4.BeautifulSoup(resp.text)
    sresult_list = html.select('li.pc-header-nav-parent')

    for i in sresult_list:
        link_text = i.select('a')[0].text
        link = i.select('a')[0]
        linked_url = link.get('href')
        top_page_links[link_text] = linked_url
    return top_page_links

@task
def get_child_page_links():
    return 1+1
    # resp = requests.get(url)
    # html = bs4.BeautifulSoup(resp.text)
    # sresult_list = html.select('section.items-box-container')
    #
    # for items in sresult_list:
    #     link_text = items.select('section.items-box')
    #     child_page_links.append(link_text)

    # return resp

