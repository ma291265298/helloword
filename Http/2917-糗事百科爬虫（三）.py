import requests
from lxml import etree
import json

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
}
url = 'https://www.qiushibaike.com/'

response = requests.get(url, headers=header)
html = response.content.decode()
element = etree.HTML(html)
lst = element.xpath('//*[@class="recommend-article"]/ul/li')
data = {}
for j in range(len(lst)):
    img = "https://" + lst[j].xpath('.//a/img/@src')[0]
    title = lst[j].xpath('.//*[@class="recmd-right"]/a/text()')[0]
    laugh = lst[j].xpath('.//*[@class="recmd-detail clearfix"]/div/span[1]/text()')[0]
    comment = lst[j].xpath('.//*[@class="recmd-detail clearfix"]/div/span[4]/text()')
    if len(comment) == 0:  # 防止出现不存在评论的情况
        comment = 0
    else:
        comment = comment[0]
    author = lst[j].xpath('.//*[@class="recmd-detail clearfix"]/a/img/@alt')[0]
    temp = {
        "title": title,
        "author": author,
        "laugh": laugh,
        "comment": comment,
        "img": img
    }
    data[j] = temp

with open('2917.json', 'w', encoding='utf-8')as f:
    f.write(json.dumps(data, ensure_ascii=False, indent=4))
