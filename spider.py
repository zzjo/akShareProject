from urllib.request import urlopen
import requests

url = "https://movie.douban.com/j/chart/top_list"
param = {
    "type": 24,
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20,
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}
resp = requests.get(url=url, params=param, headers=headers)
print(resp.json())

# url = 'http://www.baidu.com'
# resp = urlopen(url)
# # print(resp.read().decode("utf-8"))
# with open("mybaidu.html", mode="w", encoding="utf-8") as f:
#     f.write(resp.read().decode("utf-8"))
# print("over")
