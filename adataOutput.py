import codecs


class DataOutput(object):#数据存储器
    def __init__(self):
        self.datas=[]

    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout=codecs.open('baike.html','w',encoding='utf-8')
        fout.write("<html>")
        fout.write("<head><meta charset='utf-8'/></head>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            print(data["title"])
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['url'])
            fout.write("<td>%s</td>"%data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
            # self.datas.remove(data)
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
# class DataOutput(object):
#     def __init__(self):
#         self.datas = []
#
#     def store_data(self, data):
#         if data == None:
#             return
#         self.datas.append(data)
#
#     def output_html(self):
#         fout = codecs.open("output.html", "w", encoding='utf-8')
#         fout.write("<html>")
#         fout.write("<body>")
#         fout.write("<table>")
#         for data in self.datas:
#             print(data["title"])
#             fout.write("<tr>")
#             fout.write("<td>%s</td>" % data["url"])  # .encode("utf-8"))
#             fout.write("<td>%s</td>" % data["title"])  # .encode("utf-8"))
#             fout.write("<td>%s</td>" % data["summary"])  # .encode("utf-8"))
#             fout.write("</tr>")
#         fout.write("</table>")
#         fout.write("</body>")
#         fout.write("</html>")
#         fout.close()
