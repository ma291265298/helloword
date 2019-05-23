import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
key = input()
url = 'https://www.baidu.com/s?wd=' + key

response = requests.get(url, headers=headers)
print(response.status_code)

with open('2909.html', 'wb')as f:
    f.write(response.content)
