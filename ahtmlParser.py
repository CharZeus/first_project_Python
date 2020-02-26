import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup


class HtmlParser(object):
    def _get_new_data(self, page_url, soup):
        data = {}
        data['url'] = page_url
        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div', class_='lemma-summary')
        # 获取tag中包含的所有文本内容，包括子孙tag中的内容，并将结果作为Unicode字符串返回
        data['summary'] = summary.get_text()
        # print(summary_node.get_text())
        return data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # print(new_urls)
        links = soup.find_all('a', href=re.compile('/item/\w+'))

        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
            # print(new_full_url)
        return new_urls

    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')  # ,from_encoding='utf-8'
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
# import re
# from urllib.parse import urljoin
# from bs4 import BeautifulSoup
#
#
# class HtmlParser(object):
#     def parser(self, page_url, html_content):
#         if page_url == None or html_content == None:
#             return
#         soup = BeautifulSoup(html_content,"html.parser")
#         new_urls = self._get_new_urls(page_url, soup)
#         new_data = self._get_new_data(page_url, soup)
#         return new_urls, new_data
#
#     def _get_new_urls(self, page_url, soup):
#         new_urls = set()
#         links = soup.find_all('a', href=re.compile(r'/item/*'))
#         for link in links:
#             new_url = link["href"]
#             new_full_url = urljoin(page_url, new_url)
#             new_urls.add(new_full_url)
#         return new_urls
#
#     def _get_new_data(self, page_url, soup):
#         res_data = {}
#         title_node = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h1")
#         res_data["title"] = title_node.get_text()
#         summary_node = soup.find("div", class_="lemma-summary")
#         res_data["summary"] = summary_node.get_text()
#         # print(summary_node.get_text())
#         res_data["url"] = page_url
#         return res_data
