from time import time
import httpx
from urllib.parse import quote
from py_mini_racer import py_mini_racer

cookies = {
    "sessionid": "zs6sm4jn3ax9ofci8ghmboe86sn8jgxe",
}
# url转码
headers = {
    "User-Agent": "yuanrenxue.project",
}
v8 = py_mini_racer.MiniRacer()
timestamp = int(time()) * 1000
with open("q6/sign.js", "r", encoding="utf-8") as f:
    js = f.read()
    v8.eval(js)

q = ""
url = "https://match.yuanrenxue.cn/api/match/6"
sum = 0
for page in range(1, 6):
    q = q + f"{page}-{timestamp}|"
    params = {
        "page": page,
        "m": v8.call("get_m", timestamp, page),
        "q": q,
    }
    response = httpx.get(url, params=params, headers=headers, cookies=cookies)
    data = response.json()["data"]
    for i in data:
        sum += i["value"] * 24
print(sum)