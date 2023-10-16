import requests
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
from base64 import b64encode
public_key = "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDq04c6My441Gj0UFKgrqUhAUg+kQZeUeWSPlAU9fr4HBPDldAeqzx1UR99KJHuQh/zs1HOamE2dgX9z/2oXcJaqoRIA/FXysx+z2YlJkSk8XQLcQ8EBOkp//MZrixam7lCYpNOjadQBb2Ot0U/Ky+jF2p+Ie8gSZ7/u+Wnr5grywIDAQAB\n-----END PUBLIC KEY-----"
key = RSA.import_key(public_key)
encrypt = PKCS1_cipher.new(key)
result = encrypt.encrypt("1|1697186779000".encode())
print(b64encode(result))
# url = "https://match.yuanrenxue.cn/api/match/20"

# params = {
#     "page": 1,
#     "sign": "0bf0225b10ab9132c6cac25b839c5a73",
#     "t": 1697182173000,
# }
# response = requests.get(url, params=params)

# print(response.text)
