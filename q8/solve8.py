import base64
import re
import time
import httpx
import cv2
import numpy as np
from baiduapi import get_token, ocr
auth_token = get_token()

# import ddddocr

# ocr = ddddocr.DdddOcr(beta=True)


def cv_show(img, window_name="image"):
    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def remove_background(image):
    """去除前二多的颜色，即背景色"""
    image = image.copy()
    pixel = image.reshape(-1, 3)
    unique_colors, counts = np.unique(pixel, return_counts=True, axis=0)
    top2index, top1index = counts.argsort()[-2:]
    top1color = unique_colors[top1index]
    top2color = unique_colors[top2index]
    # 将这两种颜色置为白色
    mask1 = np.all((image == top1color) | (image == top2color), axis=-1)
    image[mask1] = [255, 255, 255]
    return image


def remove_lines(image):
    """二值化后去除斜线"""
    _, gray = cv2.threshold(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), 254, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2), (0, 0))
    gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    gray = cv2.bitwise_not(gray)
    # 形态学去除连通域小的噪点
    retval, labels, stats, centroids = cv2.connectedComponentsWithStats(gray, connectivity=4)
    for i in range(1, retval):
        if stats[i][4] < 50:
            gray[labels == i] = 0
        else:
            gray[labels == i] = 255
    # 去除斜线
    temp = image.copy()
    temp[gray == 0] = 255
    # 统计每种颜色的像素数量
    unique_colors, counts = np.unique(temp.reshape(-1, 3), return_counts=True, axis=0)
    result = image.copy()
    # 去除像素数量小于指定阈值的颜色
    for i in range(len(unique_colors)):
        if counts[i] > 100:
            result[(image == unique_colors[i]).all(axis=2)] = 255
    # 去除井字分割线
    result[:, 100] = 255
    result[:, 200] = 255
    result[100, :] = 255
    result[200, :] = 255
    _, gray = cv2.threshold(cv2.cvtColor(result, cv2.COLOR_BGR2GRAY), 254, 255, cv2.THRESH_BINARY)
    return gray


def remove_closed_shapes(image, threshold=160):
    small_contours = []
    contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < threshold:
            small_contours.append(contour)
    image = cv2.drawContours(image.copy(), small_contours, -1, (0, 0, 0), -1)
    return image


def erode(image):
    """对提取出的汉字进行腐蚀"""
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    gray = cv2.erode(image, kernel, iterations=3)
    # 闭合轮廓
    gray = remove_closed_shapes(gray, 100)
    gray = cv2.medianBlur(gray, 5)
    # gray = cv2.erode(gray, kernel, iterations=1)
    gray = cv2.resize(gray, (300, 300), interpolation=cv2.INTER_NEAREST)
    return gray


def split_image(image):
    """分割图片"""
    w, h = image.shape
    for y in range(0, h, h // 3):
        for x in range(0, w, w // 3):
            img = image[y : y + h // 3, x + w // 20 : x + w // 3 + w // 20]
            if img.shape[1] < 100:
                img = cv2.copyMakeBorder(img, 0, 0, 0, w // 20, cv2.BORDER_CONSTANT, value=255)
            yield img


url = "https://match.yuanrenxue.cn/api/match/8_verify"
headers = {
    "User-Agent": "yuanrenxue.project",
    "cookie": "sessionid=ceo1z4jvkkk7b1xqkoger9px9939gn7h;",
}
params = {}
nums = []
client = httpx.Client(verify=False, headers=headers, follow_redirects=True)
for i in range(5):
    res = client.get(url, params=params)
    # base64转图片
    html = res.json()["html"]
    image_base64 = re.search(r"base64,(.*?)\"", html).group(1)
    text = re.findall(r"<p>(.*?)</p>", html)
    print(text)
    image_data = base64.b64decode(image_base64)
    image_array = np.frombuffer(image_data, np.uint8)
    origin_image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    # 去除背景色
    nobg_image = remove_background(origin_image)
    # 二值化后去除斜线
    noline_image = remove_lines(nobg_image)
    noline_image = cv2.resize(noline_image, (900, 900), interpolation=cv2.INTER_NEAREST)
    result = erode(noline_image)
    for index, image in enumerate(split_image(result)):
        retval, buffer = cv2.imencode(".jpg", image)
        jpg_as_text = base64.b64encode(buffer).decode()
        time.sleep(1)
        character = ocr(jpg_as_text, auth_token)
        print(character)
        cv_show(image)
result = sum(nums)
print(result)
