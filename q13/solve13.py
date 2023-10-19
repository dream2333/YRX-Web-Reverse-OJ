import httpx
import re

url = "https://match.yuanrenxue.com/api/match/13"
url_cookies = "https://match.yuanrenxue.com/match/13"
headers = {
    "User-Agent": "yuanrenxue.project",
}
cookies = {"sessionid": "lr3c6xrlgsmagzsvqbl41ap2h33eav7n"}
nums = []
client = httpx.Client(verify=False, headers=headers, cookies=cookies, http2=True)


def get_page(page):
    params = {
        "page": page,
    }
    res = client.get(url, params=params)
    print(res.text)
    if res.is_error:
        res_cookies = client.get(url_cookies, params=params)
        groups = re.findall("\('(.)'\)", res_cookies.text)
        cookie = "".join(groups).split("=")
        client.cookies.set(cookie[0], cookie[1])
        get_page(page)
    else:
        for k in res.json()["data"]:
            nums.append(k["value"])


for i in range(5):
    get_page(i + 1)

result = sum(nums)
print(result)
