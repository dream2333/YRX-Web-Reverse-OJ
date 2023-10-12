import httpx
import random
import ssl
ORIGIN_CIPHERS = "ECDH+AESGCM"

class SSLFactory:
    def __init__(self):
        self.ciphers = ORIGIN_CIPHERS.split(":")

    def __call__(self) -> ssl.SSLContext:
        random.shuffle(self.ciphers)
        ciphers = ":".join(self.ciphers)
        ciphers = ciphers + ":!aNULL:!eNULL:!MD5"
        context = ssl.create_default_context()
        context.set_ciphers(ciphers)
        return context

cipher = SSLFactory()

headers = {
    'authority': 'match.yuanrenxue.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'cookie': 'sessionid=lr3c6xrlgsmagzsvqbl41ap2h33eav7n;',
    'pragma': 'no-cache',
    'referer': 'https://match.yuanrenxue.com/match/19',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'yuanrenxue.project',
    'x-requested-with': 'XMLHttpRequest',
}
nums = []

# proxy = {"http://": "http://127.0.0.1:8888", "https://": "http://127.0.0.1:8888"}
client = httpx.Client(verify=cipher(), headers=headers, http2=True,)
for i in range(5):
    params = {"page": i+1}
    res = client.get("https://match.yuanrenxue.com/api/match/19", params=params)
    print(res.text)
    for k in res.json()["data"]:
        nums.append(k["value"])
result = sum(nums)
print(result)
