import httpx
from lxml import etree
import base64
import hashlib

url = "https://match.yuanrenxue.com/api/match/4"
headers = {
    "User-Agent": "yuanrenxue.project",
    "cookie": "sessionid=0lu5c2vi26o5qj5vxo4dbmb8p98818q0;",
    "accept": "*/*",
    "referer": "https://match.yuanrenxue.com/match/3",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
}
nums = []


def get_j_key(key, value):
    content = base64.b64encode((key + value).encode("utf8")).replace(b"=", b"")
    return hashlib.md5(content).hexdigest()


client = httpx.Client(verify=False, headers=headers, http2=True)
num_map = {}
for i in range(5):
    res = client.get(url, params={"page": i + 1})
    result = res.json()
    dom = etree.HTML(result["info"])
    j_key = get_j_key(result["key"], result["value"])
    for td in dom.xpath("//td"):
        temp = []
        origin = 0
        for img in td.xpath("./img"):
            image = img.xpath("./@src")[0].split(",")[1]
            offsite:str = img.xpath("./@style")[0]
            offsite = origin + float(offsite.removeprefix("left:").removesuffix("px"))
            cssclass = img.xpath("./@class")[0]
            if "img_number " + j_key == cssclass:
                continue
            with open("num.jpg", "wb") as f:
                f.write(base64.b64decode(image))
            if image not in num_map:
                num_map[image] = int(input("输入数字："))
            temp.append((num_map[image],offsite))
            origin+=11.5
        print(temp)
        temp = sorted(temp,key=lambda x:x[1])
        print(temp)
        num = 0
        for n,_ in temp:
            num = num*10+n
        print(num)
        nums.append(num)
print(nums)
result = sum(nums)
print(result)
