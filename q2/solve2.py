import httpx
from py_mini_racer import MiniRacer

url = "https://match.yuanrenxue.com/api/match/2"
headers = {
    "User-Agent": "yuanrenxue.project",
}
cookies = {
    "sessionid": "zs6sm4jn3ax9ofci8ghmboe86sn8jgxe",
    "m": "",
}
v8 = MiniRacer()
with open("q2/sign.js", "r", encoding="utf-8") as f:
    js = f.read()
    v8.eval(js)
cookies["m"] = v8.call("get_m")
nums = []
client = httpx.Client(verify=False, headers=headers, cookies=cookies)
for i in range(5):
    params = {
        "page": i + 1,
    }
    res = client.get(url, params=params, follow_redirects=True)
    print(res.text)
    nums.extend([k["value"] for k in res.json()["data"]])
result = sum(nums)
print(result)
