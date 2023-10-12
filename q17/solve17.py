import httpx
import re

url = "https://match.yuanrenxue.com/api/match/17"
headers = {
    "User-Agent": "yuanrenxue.project",
    # "accept": "application/json, text/javascript, */*; q=0.01",
}
cookies = {"sessionid": "lr3c6xrlgsmagzsvqbl41ap2h33eav7n"}
cookies2 = None
nums = []
proxy = {"https://": "http://127.0.0.1:8888"}
client = httpx.Client(
    verify=False, headers=headers, cookies=cookies, proxies=proxy, http2=True
)


def get_page(page):
    params = {
        "page": page,
    }
    res = client.get(url, params=params)
    print(res.text)
    for k in res.json()["data"]:
        nums.append(k["value"])


for i in range(5):
    get_page(i + 1)

result = sum(nums)
print(result)
