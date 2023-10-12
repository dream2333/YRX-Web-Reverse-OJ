import httpx
import base64

url = "https://match.yuanrenxue.com/api/match/12"
headers = {
    "User-Agent": "yuanrenxue.project",
    "cookie": "sessionid=lr3c6xrlgsmagzsvqbl41ap2h33eav7n;",
}
nums = []
proxy = {"https://": "http://127.0.0.1:8888"}
client = httpx.Client(verify=False, headers=headers, proxies=proxy,)
for i in range(5):
    params = {
        "page": i + 1,
        "m": base64.b64encode(f"yuanrenxue{i+1}".encode("ascii")).decode("utf8"),
    }
    res = client.get(url, params=params)
    print(res.text)
    for k in res.json()["data"]:
        nums.append(k["value"])

result = sum(nums)
print(result)
