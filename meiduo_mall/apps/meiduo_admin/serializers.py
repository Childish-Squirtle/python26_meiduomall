
from rest_framework import serializers


# 登陆的逻辑，主要目的在与签发jwt_token
# 1、用户名和密码验证（用户名有可能是手机号）
# 2、签发token
class JSONWebTokenSerializer(serializers.Serializer):
    # 需要反序列化校验的数据
    username = serializers.CharField(required=True, max_length=100)
    # 只需要在反序列化的时候进行数据的校验，不需要序列化返回给前端， write_only=True
    password = serializers.CharField(required=True, write_only=True)

    # 需要序列化给前端的数据
    # ------1-----
    # user_id = serializers.IntegerField(read_only=True)
    # token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        # 1、用户名和密码验证（用户名有可能是手机号）
        username = attrs["username"]
        password = attrs['password']

        # 获得一个用户对象
        user = authenticate(username=username, password=password)
        if not user:
            # user为空
            raise serializers.ValidationError("用户身份验证失败！")


        # 2、构建出一个token


        # 传入user用户对象，根据用户对象，构建载荷数据
        # {
        #    "username": "xxx",
        #    "user_id": "xxx"
        # }
        # payload = "fgewgegwrwhtwnyjrwtwhjytjwyjwj"
        payload = jwt_payload_handler(user)

        # 构建token
        token = jwt_encode_handler(payload)


        return {
            "user": user,
            "token": token
        }


        # validate函数返回什么数据，最终通过serializer.data序列化的就是什么数据
        # ------1-----
        # return {
        #     "username": user.username,
        #     "user_id": user.id,
        #     "token": token
        # }
