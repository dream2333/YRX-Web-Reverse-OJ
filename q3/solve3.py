import httpx
from collections import Counter

urljssm = "https://match.yuanrenxue.com/jssm"
urlmatch = "https://match.yuanrenxue.com/api/match/3"
headers = {
    "User-Agent": "yuanrenxue.project",
    "cookie": "sessionid=lr3c6xrlgsmagzsvqbl41ap2h33eav7n;",
    "accept": "*/*",
    "referer": "https://match.yuanrenxue.com/match/3",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
}
id = []

client = httpx.Client(verify=False, headers=headers, http2=True)
for i in range(5):
    res = client.post(urljssm, headers=headers)
    res = client.get(urlmatch, params={"page": i + 1})
    print(res.text)
    for k in res.json()["data"]:
        id.append(k["value"])

result = Counter(id).most_common(1)[0][0]
print(result)
