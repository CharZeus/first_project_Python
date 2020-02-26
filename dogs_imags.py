import requests
import bs4
from lxml import etree

url = 'https://www.uumtu.com/zt/gougoutupian.html'
html = requests.get(url)
result0 = etree.HTML(html.text)