import execjs
import time
import sys
import httpx

with open(sys.path[0] + "/webpack.js", "r") as f:
    js = f.read()


def get_m():
    jsobject = execjs.compile(js)
    m = jsobject.call("get_result")
    return m


url = "https://match.yuanrenxue.com/api/match/16"
headers = {
    "User-Agent": "yuanrenxue.project",
    "cookie": "sessionid=atbbm0no2jettlifpb1os63ybtv12v8v;",
    "accept": "*/*",
    "referer": "https://match.yuanrenxue.com/match/16",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
}
prices = []
for i in range(5):
    t, m = get_m()
    params = {"t": t, "m": m, "page": i + 1}
    res = httpx.get(url, params=params, headers=headers)
    for k in res.json()["data"]:
        prices.append(k["value"])

result = sum(prices)
print(result)
