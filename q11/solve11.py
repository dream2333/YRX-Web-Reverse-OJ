import base64
import httpx
import random


# 本题难点在于native方法反汇编，所以需要先反汇编找到算法，jni_load中可以找到一个自定义的base64编码，实现自定义的base64编码
def custom_base64(data):
    # 算法难点在于更换了base64的字符表,并将每四个字符一组的字符中的第2个与第3个互换
    origin_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    custom_table = "9+#FvwxNG78pqrghijCDEWXy4oAd56kQHlmBuOPYz0cstef1IJKLM23ZabnRSTUV"
    # 由于base64的字符表是固定的，所以可以通过替换字符表的方式来实现自定义base64编码
    trans = str.maketrans(origin_table, custom_table)
    encoded_data = base64.b64encode(data.encode()).decode().translate(trans)
    # 将每四个字符一组的字符中的第2个与第3个互换
    ret = ""
    for i in range(0, len(encoded_data), 4):
        group = encoded_data[i : i + 4]
        if len(group) == 4:
            group = group[0] + group[2] + group[1] + group[3]
        ret += group
    return ret


def main():
    client = httpx.Client(http2=True, verify=False, follow_redirects=True)
    url = "https://match.yuanrenxue.com/api/match/11/query"
    sum = 0
    for num in range(0, 100):
        n1 = random.randint(0, 10000)
        n2 = random.randint(0, 1000000)
        n3 = random.randint(0, 120)
        # 原始的字符串为："%d:yuanrenxue2020:%ld:randomClientId%sReplaceWithYourTeamNameIfYouCrackedToHere"
        # ReplaceWithYourTeamNameIfYouCrackedToHere不做校验，可以省略掉
        encrypt_sign = f"{n1}:yuanrenxue2020:{num}:randomClientId{n2}"
        for i in encrypt_sign:
            i = ord(i) ^ 0x14
            encrypt_sign = encrypt_sign + chr(i)
        encrypt_sign = str(chr(n3)) + encrypt_sign
        encrypt_sign = custom_base64(encrypt_sign)
        params = {"id": num, "sign": encrypt_sign}
        response = client.get(url, params=params)
        sum = sum + response.json()["data"]
        print(response.text)
    print(sum)


if __name__ == "__main__":
    main()
