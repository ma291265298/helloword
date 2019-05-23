import requests
import json

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
key = input('请输入要翻译的单词：')
data = {
    'i': key,
    'from': 'AUTO',
    'to': 'AUTO',
    'doctype': 'json'
}
response = requests.post(url, data=data, headers=headers)
data = response.content.decode()
data_dict = json.loads(data)
s = data_dict['translateResult'][0][0]
print(s['tgt'])
