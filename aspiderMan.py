# coding:utf-8
from craw_pratice.adataOutput import DataOutput
from craw_pratice.ahtmlDownloader import HtmlDownloader
from craw_pratice.ahtmlParser import HtmlParser
from craw_pratice.aurlManeger import UrlManager


class spiderman(object):
    def __init__(self):
        self.manage = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        self.manage.add_new_url(root_url)
        # 判断URL管理器中是否有新的URL，同时判断抓去了多少个URL
        while (self.manage.has_new_url() and self.manage.old_url_size() < 10):
            try:
                new_url = self.manage.get_new_url()  # 从管理器获取新的URL
                print("已经抓取%s个链接: %s" % (self.manage.old_url_size(), new_url))
                # print("craw %d : %s" % (self.manage.old_url_size(), new_url))
                html = self.downloader.download(new_url)  # 下载网页
                print(html)
                new_urls, data = self.parser.parser(new_url, html)  # 解析器抽取网页数据
                # print("ok")
                self.manage.add_new_urls(new_urls)
                self.output.store_data(data)  # 存储
            except Exception:
                print("crawl failed")
        self.output.output_html()


if __name__ == "__main__":
    root_url = 'https://baike.baidu.com/item/Python/407313'  # 'https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB'
    spider_man = spiderman()
    spider_man.crawl(root_url)  # ("https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB")
# from craw_pratice.adataOutput import HtmlOutputer
# from craw_pratice.ahtmlDownloader import HtmlDownloader
# from craw_pratice.ahtmlParser import HtmlParser
# from craw_pratice.aurlManeger import UrlManager
#
#
# class SpiderMain(object):
#     def __init__(self):
#         self.manage = UrlManager()
#         self.downloader = HtmlDownloader()
#         self.parser = HtmlParser()
#         self.outputer = DataOutput()
#
#     def craw(self, root_url):
#         count = 1
#         self.manage.add_new_url(root_url)
#         while self.manage.has_new_url()and self.manage.old_url_size() < 10:
#             try:
#                 new_url = self.manage.get_new_url()
#                 print("craw %d : %s" % (count, new_url))
#                 count += 1
#                 html_content = self.downloader.download(new_url)
#                 new_urls, new_data = self.parser.parser(new_url, html_content)
#                 self.manage.add_new_urls(new_urls)
#                 # print(new_urls)
#                 self.outputer.store_data(new_data)
#                 # if count == 20:
#                 #     break
#             except:
#                 print("craw failed")
#         self.outputer.output_html()
#
#
# if __name__ == "__main__":
#     root_url = 'https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB'#"https://baike.baidu.com/item/Python/407313"
#     obj_spider = SpiderMain()
#     obj_spider.craw(root_url)
