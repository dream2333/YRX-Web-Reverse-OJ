import httpx
import execjs


url = "https://match.yuanrenxue.com/api/match/5"
headers = {
    "User-Agent": "yuanrenxue.project",
}

with open("q5/sign.js", "r", encoding="utf-8") as f:
    js = execjs.compile(f.read())
cookies, params = js.call("getSign")
cookies["sessionid"] = "zs6sm4jn3ax9ofci8ghmboe86sn8jgxe"

client = httpx.Client()
nums = []
for i in range(5):
    params["page"] = i + 1
    res = client.get(url, params=params, cookies=cookies)
    print(res.json())
    for j in res.json()["data"]:
        nums.append(j["value"])
nums = sorted(nums, reverse=True)
print(sum(nums[0:5]))
