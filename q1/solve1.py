import execjs
import time
import sys
import httpx

with open(sys.path[0] + "/hash.js", "r") as f:
    js = f.read()


def get_m():
    timestamp = int(time.time()) * 1000 + 100000000
    jsobject = execjs.compile(js)
    m = jsobject.call("hex_md5", "%d" % timestamp) + "丨" + "%d" % (timestamp / 1000)
    return m


url = "https://match.yuanrenxue.com/api/match/7"
headers = {"User-Agent": "yuanrenxue.project"}
prices = []
for i in range(5):
    params = {"m": get_m(), "page": i + 1}
    res = httpx.get(url, params=params, headers=headers)
    for k in res.json()["data"]:
        prices.append(k["value"])

result = sum(prices)/len(prices)
print(result)
