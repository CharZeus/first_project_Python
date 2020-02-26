import requests
import bs4

def spider_bs4_demo(URL):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '#Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)
    headers = {'User-Agent': user_agent}
    html = requests.get(URL, headers=headers)
    html_contents = html.text
    # print(type(html_contents))
    soup = bs4.BeautifulSoup(html_contents, 'html.parser')
    count_pdf = 0
    count_pptx = 0
    count_video = 0
    count = 0
    file = open('speech_copy.txt', 'a', encoding='UTF-8')
    list_pdf = []
    list_pptx = []
    list_video = []
    for link in soup.find_all('a', string=['pdf', 'pptx', 'video']):
        count += 1
        # file.write(str(count)+': http://speech.ee.ntu.edu.tw/~tlkagk/' + link.get("href")+'\n')
        if 'pptx' in link.get('href'):
            count_pptx += 1
            list_pptx.append(link.get('href'))
        elif 'pdf' in link.get('href'):
            count_pdf += 1
            list_pdf.append(link.get('href'))
        else:
            count_video += 1
            list_video.append(link.get('href'))
    for i in range(len(list_pptx)):
        print("ppt课件" + str(i + 1) + ': http://speech.ee.ntu.edu.tw/~tlkagk/' + list_pptx[i] + '\n')
        # file.write("ppt课件" + str(i + 1) + ': http://speech.ee.ntu.edu.tw/~tlkagk/' + list_pptx[i] + '\n')
    for i in range(len(list_pdf)):
        print("pdf文档" + str(i + 1) + ': http://speech.ee.ntu.edu.tw/~tlkagk/' + list_pdf[i] + '\n')
        # file.write("pdf文档" + str(i + 1) + ': http://speech.ee.ntu.edu.tw/~tlkagk/' + list_pdf[i] + '\n')
    for i in range(len(list_video)):
        print("课程视频" + str(i + 1) + ': http://speech.ee.ntu.edu.tw/~tlkagk/' + list_video[i] + '\n')
        # file.write("课程视频" + str(i + 1) + ': http://speech.ee.ntu.edu.tw/~tlkagk/' + list_video[i] + '\n')

if __name__=="__main__":
    url= 'http://speech.ee.ntu.edu.tw/~tlkagk/courses_ML17.html'
    spider_bs4_demo(url)
# print(list_pdf)
# print(str(count_video)+" "+str(count_pdf)+" "+str(count_pptx))
