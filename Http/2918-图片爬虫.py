import requests
from lxml import etree

import os

if not os.path.exists('2918'):
    os.mkdir('2918')
os.chdir('2918')

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
}
tmp_url = 'https://list.jd.com/list.html?cat=9987,653,655&page='
for i in range(1, 2):
    url = tmp_url + str(i)
    response = requests.get(url, headers=header)
    html = response.content.decode()
    element = etree.HTML(html)
    lst = element.xpath('//*[@class="p-img"]/a/img/@data-lazy-img | @src')
    for j in range(len(lst)):
        img_url = 'https:' + lst[j]
        response = requests.get(img_url, headers=header)
        with open(str(i) + '_' + str(j + 1) + '.jpg', 'wb') as f:
            f.write(response.content)
