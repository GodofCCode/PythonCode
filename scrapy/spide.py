import requests
from lxml import etree


header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}

imgPath = 'imgpath/1.jpg'

def load_page(url):
    #encode = requests.get(url, headers = header).apparent_encoding
    response = requests.get(url, headers = header)
    response.encoding = 'UTF-8-SIG'
    parse_page(response)
    return response

def parse_page(page):
    tree = etree.HTML(page.text)
    img = tree.xpath('/html/body/div[2]/div/div[2]/div/img/@src')
    #img = str(tree.xpath('/html/body/section/div/div/article/p[3]/img/@src'))
    img = img.strip('[\'')
    img = img.strip('\']')
    with open(imgPath, 'wb') as file:
        pic = requests.get(img, headers = header).content
        file.write(pic)

url = 'http://fdcfdc.49.webidc.pw/maijiaxiu/'
uri = 'http://zhainanba.net/23196.html'


load_page(url)