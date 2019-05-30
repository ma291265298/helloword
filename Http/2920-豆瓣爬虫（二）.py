import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
}

data = {
    'page_limit': 20,
    'page_start': 0
}
url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend'
response = requests.get(url, headers=headers, data=data)
html = response.content.decode()
print(len(html))
data_dict = json.loads(html)
lst = data_dict['subjects']
with open('2920.json', 'w', encoding='utf-8')as f:
    f.write(json.dumps(lst, ensure_ascii=False, indent=2))
