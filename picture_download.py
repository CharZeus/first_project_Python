import bs4
import requests
import urllib.request

imglist = []
imgname = []
count = 0

for i in range(1, 5):
    url = 'https://www.uumtu.com/zt/xiaomaotupian/' + str(i) + '.html'
    html_con = requests.get(url).content
    soup = bs4.BeautifulSoup(html_con, 'html.parser')
    # for title in soup.find_all('a', class_='taglisthtitle'):
    # print(type(title.string))

    for imglink in soup.find_all('img'):

        imgstr = str(imglink.get('data-original'))
        if imgstr != 'None':
            imglist.append(imgstr)
            imgname.append(str(imglink.get('alt')))
            count += 1
print(type(imgname[1]))
print(count)
# for imgurl in imglist:
print(imglist[0])
x = 0
for name in imgname:
    imgname = "D:/JD_image/animals_name/" + name + ".jpg"
    f=open(imgname,'wb')
    re1=requests.get(imglist[x])
    f.write(re1.content)
    # urllib.request.urlretrieve(imgurl, filename=imgname)
    x += 1
