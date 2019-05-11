from django.contrib.auth.backends import ModelBackend
from django.http import HttpRequest
import re
from users.models import User


class MeiduoModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):

        # 前台占站点登陆调用的时候 request对象不为空（存在的）
        # 后台站点登陆调用的时候，request对象为空

        try:

            user = User.objects.get(username=username)
        except:
            # 如果未查到数据，则返回None，用于后续判断
            try:
                user = User.objects.get(mobile=username)
            except:
                return None


        # 得到了一个用户对象
        # 判断该用户是不是super用户，如果是才可以访问后台管理站点
        # 直接判断is_superuser，或导致普通用户无法登陆前台站点
        # if not user.is_superuser:
        #     return None


        if request == None:
            # 后台请求
            # 判断是不是superuser
            if not user.is_superuser: # user.is_staff
                return None

        # 判断密码
        if user.check_password(password):
            return user
        else:
            return None

