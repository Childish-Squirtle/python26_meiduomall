
import json
import base64
from datetime import datetime,timedelta
import time

header = {
  "typ": "JWT",
  "alg": "SHA256"
}

header = json.dumps(header)
header = base64.b64encode(header.encode()).decode()
print("header: ", header)

# timedelta类型表示的是一个时间段对象： 365天
EXPIRATION_DELTA = timedelta(days=365)
# datetime.now()返回一个datetime类型数据：表示一个时间点； 比如 datetime(2019,10,10)
CUR_DATETIME = datetime.now()
# expire是一个datetime类型（一个时间点） datetime(2020,10,10)
expire = CUR_DATETIME+EXPIRATION_DELTA


payload = {
  "username": "weiwei",
  "user_id": 18,
  "sex": 1,
  # "expire": expire # datetime无法通过json模块dumps，所以要格式转换datetime转为字符串
  "expire": expire.strftime("%Y-%m-%d"),
}

payload = json.dumps(payload)
payload = base64.b64encode(payload.encode()).decode()
print("payload: ", payload)


import hashlib,hmac

SECRET_KEY = 'j*h(69kj^)ofyw+re!3!fpsh28a^wnm9iv1xv@9mi%^$)(dgm='
message = header + '.' + payload
sh256obj = hmac.new(SECRET_KEY.encode(), message.encode(), digestmod=hashlib.sha256)
signature = sh256obj.hexdigest()
print("signature: ", signature)

print("\n------JWT_Token-----")
JWT_Token = header + '.' + payload + '.' + signature
print("JWT_Token: ", JWT_Token)


print("\n-----JWT_Token返回给浏览器-----")

print("\n-----浏览器再一次访问，并携带了JWT_Token-----")

# 模拟前端传来的token被篡改了
JWT_Token_from_fontend = JWT_Token
# JWT_Token_from_fontend = "123.456.789"


# 从JWT_Token_from_fontend提取header、payload、signature
jwt_list = JWT_Token_from_fontend.split('.')
# print(jwt_list)
header_from_fontend = jwt_list[0]
print("header_from_fontend: ", header_from_fontend)
payload_from_fontend = jwt_list[1]
print("payload_from_fontend: ", payload_from_fontend)
signature_from_fontend = jwt_list[2]
print("signature_from_fontend: ", signature_from_fontend)

message = header_from_fontend + '.' + payload_from_fontend
sha256obj = hmac.new(SECRET_KEY.encode(), message.encode(), digestmod=hashlib.sha256)
signature_back = sha256obj.hexdigest()

print("\n----两个签名比对-----")
# if signature == signature_back:
if hmac.compare_digest(signature, signature_back):
  print("数据完整！")

  header = base64.b64decode(header_from_fontend.encode())
  payload = base64.b64decode(payload_from_fontend.encode())

  header = json.loads(header.decode())
  payload = json.loads(payload.decode())

  print(header)
  print(payload)

  expire = payload['expire'] # string："2020-10-10" ---> datetime类型
  expire = datetime.strptime(expire, "%Y-%m-%d") # datetime时间点对象


  cur_time = datetime.now()

  print("当前时间: ", cur_time)
  print("有效期： ", expire)

  if cur_time > expire:
    print("过期了！")
  else:
    print("没过期！")

else:
  print("数据校验失败！")
