# # import urllib.request
# import requests#使用requests包爬取，结果提示页面不存在
#
# class HtmlDownloader(object):  # HTML下载器
#     def download(self, url):
#         if url is None:
#             return None
#         # user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
#         # headers = {'User-Agent': user_agent}
#         respondse = requests.get(url)#, headers=headers)
#         # print(url)
#         if respondse.status_code != 200:
#             return None
#         # respondse.encoding = 'utf-8'
#         # print(respondse.content)
#         return respondse.content

import urllib.request

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        headers = {'User-Agent': user_agent}
        html_content = urllib.request.Request(url,headers=headers)#urlopen(url)
        response=urllib.request.urlopen(html_content)
        if response.getcode() == 200:
            # print(response.read())
            return response.read()#.decode('utf-8')
        return None