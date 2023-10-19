import base64
import copy
import httpx
from fontTools.ttLib import TTFont

url = "https://match.yuanrenxue.com/api/match/7"
headers = {"User-Agent": "yuanrenxue.project"}
params = {"page": "1"}
cookies = {"sessionid": "5iaewlhfu6kkhfij80wmud9bveeornwa"}
client = httpx.Client(http2=True, verify=False, headers=headers, follow_redirects=True)
num_max = 0


# font的标识到数字的映射
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
usernames = [
    "爷灬霸气傀儡",
    "梦战苍穹",
    "傲世哥",
    "мaη肆風聲",
    "一刀メ隔世",
    "横刀メ绝杀",
    "Q不死你R死你",
    "魔帝殤邪",
    "封刀不再战",
    "倾城孤狼",
    "戎马江湖",
    "狂得像风",
    "影之哀伤",
    "謸氕づ独尊",
    "傲视狂杀",
    "追风之梦",
    "枭雄在世",
    "傲视之巅",
    "黑夜刺客",
    "占你心为王",
    "爷来取你狗命",
    "御风踏血",
    "凫矢暮城",
    "孤影メ残刀",
    "野区霸王",
    "噬血啸月",
    "风逝无迹",
    "帅的睡不着",
    "血色杀戮者",
    "冷视天下",
    "帅出新高度",
    "風狆瑬蒗",
    "灵魂禁锢",
    "ヤ地狱篮枫ゞ",
    "溅血メ破天",
    "剑尊メ杀戮",
    "塞外う飛龍",
    "哥‘K纯帅",
    "逆風祈雨",
    "恣意踏江山",
    "望断、天涯路",
    "地獄惡灵",
    "疯狂メ孽杀",
    "寂月灭影",
    "骚年霸称帝王",
    "狂杀メ无赦",
    "死灵的哀伤",
    "撩妹界扛把子",
    "霸刀☆藐视天下",
    "潇洒又能打",
    "狂卩龙灬巅丷峰",
    "羁旅天涯.",
    "南宫沐风",
    "风恋绝尘",
    "剑下孤魂",
    "一蓑烟雨",
    "领域★倾战",
    "威龙丶断魂神狙",
    "辉煌战绩",
    "屎来运赚",
    "伱、Bu够档次",
    "九音引魂箫",
    "骨子里的傲气",
    "霸海断长空",
    "没枪也很狂",
    "死魂★之灵",
]
usernames = copy.deepcopy(usernames[::-1])
user_max = ""
for i in range(5):
    params["page"] = i + 1
    res = client.get(url, headers=headers, params=params, cookies=cookies)
    data = res.json()
    font_data = base64.b64decode(data["woff"])
    with open("q7/font.woff", "wb") as f:
        f.write(font_data)
    # TTFont打开字体文件
    font = TTFont("q7/font.woff")
    font.saveXML("q7/font.xml")
    # 找出当前字体到数字的映射关系
    current_font_map = {}
    for name, glyph in font["glyf"].glyphs.items():
        if name == ".notdef":
            continue
        flag = bytes(glyph.flags).hex()
        current_font_map[name[3:]] = font_map[flag]
    # 对加密的数字进行解密
    print(f"第{i+1}页的数字:")
    for num in data["data"]:
        digits = num["value"].replace("&#x", "").split()
        num_decode = int("".join([current_font_map[i] for i in digits]))
        username = usernames.pop()
        print(username, num_decode)
        if num_max < num_decode:
            num_max = num_decode
            user_max = username


print("最大数:", user_max, num_max)
