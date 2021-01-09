from bs4 import BeautifulSoup
import requests


def apstrada_datni(datne, encoding='utf-8'):
    with open(datne) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    return soup


def apstrada_lapu(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup