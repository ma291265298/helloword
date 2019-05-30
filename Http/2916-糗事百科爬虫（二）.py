import requests
from lxml import etree

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
}
tmp_url = 'https://www.qiushibaike.com/hot/page/'
for i in range(1, 2):
    url = tmp_url + str(i)
    response = requests.get(url, headers=header)
    html = response.content.decode()
    element = etree.HTML(html)
    lst = element.xpath('//*[@class="content"]/span[1]')

    for j in range(len(lst)):
        print('第' + str(i) + '页，第' + str(j + 1) + '则 :')
        content = lst[j].xpath('string(.)')  # 用这种方法不会出现由于<br>标签的换行导致信息不匹配
        content = content.replace('\n', '')
        content = content.replace('<br/>', '\n')
        print(content + '\n')
