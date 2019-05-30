import requests
import re
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
}

url = 'https://movie.douban.com/chart'

response = requests.get(url, headers=headers)
html = response.content.decode()
element = etree.HTML(html)
lst = element.xpath('//*[@class="item"]')
pat = r'(\d*)人评价'
for movie in lst:
    title = movie.xpath('.//td/a/@title')[0]
    href = movie.xpath('.//td/a/@href')[0]
    img_url = movie.xpath('.//td/a/img/@src')[0]
    comment = movie.xpath('.//*[@class="star clearfix"]/span[3]/text()')
    comment = re.compile(pat).findall(comment[0])[0]
    score = movie.xpath('.//*[@class="star clearfix"]/span[2]/text()')[0]
    print('title:'+title)
    print('href:'+href)
    print('img_url:'+img_url)
    print('score:'+score)
    print('comment:'+comment+'\n')
    # print(title, href, img_url, score, comment)
