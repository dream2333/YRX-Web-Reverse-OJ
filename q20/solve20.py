import time
import httpx
from hashlib import md5

cookies = {
    "sessionid": "x209bybvz4p1fbfpwnjn7tospd52pjph",
}
# url转码
headers = {
    "User-Agent": "yuanrenxue.project",
}
salt = "D#uqGdcw41pWeNXm"
sum = 0
for page in range(1, 6):
    timestamp = int(time.time()) * 1000
    sign = md5(f"{page}|{timestamp}{salt}".encode()).hexdigest()
    params = {
        "page": page,
        "sign": sign,
        "t": timestamp,
    }
    response = httpx.get(
        "https://match.yuanrenxue.cn/api/match/20", params=params, headers=headers, cookies=cookies
    )
    print(response.text)
    data = response.json()["data"]
    for i in data:
        sum += i["value"]
print(sum)
