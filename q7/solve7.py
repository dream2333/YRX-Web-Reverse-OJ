import base64
from io import BytesIO
import requests
from fontTools.ttLib import TTFont

url = "https://match.yuanrenxue.com/api/match/7"
headers = {"User-Agent": "yuanrenxue.project"}
params = {"page": "1"}
cookies = {"sessionid": "zs6sm4jn3ax9ofci8ghmboe86sn8jgxe"}
client = requests.Session()
nums = []

# font的标识和数字的映射
font_map = {
    "01000001010001010101": "1",
    "010001000100010001010001000100000001000100010001010001000100010001000100000100000100000100010001000001000000000100": "8",
    "010101010101010101010101010101": "4",
    "0100000100010001000001010100010001000101000100010001000100010001000000010000010000": "9",
    "01010100010001000001000001000100010100010001000100010000010001000101010101": "5",
    "0100010000010000010000010001000100000100000100000100": "0",
    "0100010001010000010001000000010101010000000100010001000101000100010000010001000100010000": "3",
    "010000010100010001000001000100010001000101010100010001000000": "2",
    "01010101010101": "7",
    "0100010001000100010000000001000100010101000100010001010001000100000100010001000000": "6",
}

font_map = {v: k for k, v in font_map.items()}
print(font_map)
for i in range(5):
    params["page"] = i + 1
    res = client.get(url, params=params, cookies=cookies)
    data = res.json()
    font_data = base64.b64decode(data["woff"])
    f = BytesIO(font_data)
    with open("q7/font.woff", "wb") as f:
        f.write(font_data)
    # TTFont打开字体文件
    font = TTFont("q7/font.woff")
    for name, glyph in font["glyf"].glyphs.items():
        flag = bytes(glyph.flags)
        print(name, flag.hex())
    breakpoint()
