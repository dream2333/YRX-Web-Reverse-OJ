import httpx
from secret_key import API_KEY, SECRET_KEY

"""
通用文字识别（高精度版）
"""


def get_token():
    host = (
        "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}"
    )
    response = httpx.get(host.format(API_KEY, SECRET_KEY))
    if response:
        return response.json()['access_token']


# 二进制方式打开图片文件
def ocr(img, token):
    params = {"image": img}
    access_token = token
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    request_url = request_url + "?access_token=" + access_token
    headers = {"content-type": "application/x-www-form-urlencoded"}
    response = httpx.post(request_url, data=params, headers=headers)
    if response:
        return response.json()

