import requests
import Http.config

url = 'http://www.renren.com/PLogin.do'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
data = {
    'email': Http.config.photo,
    'password': Http.config.pw
}
response = requests.post(url, data=data, headers=headers)
print(response.status_code)

with open('2910.html', 'wb')as f:
    f.write(response.content)
