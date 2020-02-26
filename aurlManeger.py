class UrlManager():  # URL管理器
    def __init__(self):
        self.new_urls = set()  # 未爬取集合（去重）
        self.old_urls = set()

    def has_new_url(self):
        return self.new_url_size() != 0  # 判断是否有未爬取

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):  # 将新的URL添加到未爬取集合
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)


    def new_url_size(self):
        # print(len(self.new_urls))
        return len(self.new_urls)


    def old_url_size(self):
        return len(self.old_urls)
# class UrlManager(object):
#
#     def __init__(self):
#         self.new_urls = set()
#         self.old_urs = set()
#
#     def add_new_url(self, url):
#         if url is None:
#             return
#         if url not in self.new_urls and url not in self.old_urs:
#             self.new_urls.add(url)
#
#     def add_new_urls(self, urls):
#         if urls is None or len(urls) == 0:
#             return
#         else:
#             for url in urls:
#                 self.add_new_url(url)
#
#     def has_new_url(self):
#         return len(self.new_urls) != 0
#
#     def get_new_url(self):
#         new_url  = self.new_urls.pop()
#         self.old_urs.add(new_url)
#         return new_url