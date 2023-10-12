import random
import httpx
import pywasm
import sys
import time


vm = pywasm.load(sys.path[0] + "/main.wasm")


def decode():
    t1 = int(time.time()) // 2
    t2 = int(time.time()) // 2 - random.randrange(1, 51)
    return f'{vm.exec("encode",[t1,t2])}|{t1}|{t2}'


url = "https://match.yuanrenxue.com/api/match/15"
headers = {
    "authority": "match.yuanrenxue.com",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cookie": "Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1671095916; sessionid=lr3c6xrlgsmagzsvqbl41ap2h33eav7n; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1671095776,1671130132; qpfccr=true; no-alert3=true; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1671095787,1671133309; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1671133321; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1671136385",
    "referer": "https://match.yuanrenxue.com/match/15",
    "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "User-Agent": "yuanrenxue.project",
}

nums = []

client = httpx.Client(headers=headers, http2=True)
for i in range(5):
    params = {
        "m": decode(),
        "page": i + 1,
    }
    res = client.get(url, params=params)
    
    print(res.text)
    for k in res.json()["data"]:
        nums.append(k["value"])

result = sum(nums)
print(result)
