import re
import requests

pat = '<div class="content".*?<span>(.*?)</span>'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
tmp_url = 'https://www.qiushibaike.com/hot/page/'
for i in range(1, 14):
    url = tmp_url + str(i)
    response = requests.get(url, headers=header)
    html = response.content.decode()
    lst = re.compile(pat, re.S).findall(html)  # re.S编译标志，表示.也可以匹配换行符
    for j in range(len(lst)):
        print('第' + str(i) + '页，第' + str(j + 1) + '则 ')
        content = lst[j]
        content = content.replace('\n', '')
        content = content.replace('<br/>', '\n')
        print(content)
        print('')
