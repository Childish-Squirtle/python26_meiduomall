from django.shortcuts import render
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.views import APIView
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework_jwt.utils import jwt_encode_handler,jwt_payload_handler
# Create your views here.




from users.models import User
from datetime import timedelta,date,datetime
from rest_framework.permissions import IsAdminUser
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView


class UserTotalSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    date = serializers.DateField()

from django.utils import timezone
class UserTotalCountView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 用户数量
        # 日期
        count = User.objects.all().count()
        cur_date = datetime.now().today()


        s = UserTotalSerializer(data={
            "count": count,
            "date": cur_date
        })
        s.is_valid()
        return Response(s.data)

import pytz
class UserDayIncreCountView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        cur_date = datetime.now().date() # datetime.now().today()

        queryset = User.objects.filter(date_joined__gte=cur_date)
        return Response({
            "count": queryset.count(),
            "date": cur_date, # cur_date.strftime("%Y-%m-%d")
        })



class UserActiveCountView(APIView):
    permission_classes = [IsAdminUser]
    # GET
    # /meiduo_admin/statistical/day_active/
    # {
    #   "count": xxx,
    #   "date": xxx
    # }
    def get(self, request):
        cur_date = datetime.now().date() # 2019-5-17 00:00:00
        queryset = User.objects.all().filter(last_login__gte=cur_date)
        return Response({
            "count": queryset.count(),
            "date": cur_date.strftime("%Y-%m-%d")
        })


from orders.models import OrderInfo
class UserOrderCountView(APIView):
    permission_classes = [IsAdminUser]
    # GET
    # /meiduo_admin/statistical/day_orders/
    # {
    #   "count": 下单量
    #   "date"： 日期
    # }
    def get(self, request):
        # 找到所有的订单
        # 过滤出当天的订单
        # 在当天的订单中，查询出下单用户数
        # 返回下单人数
        cur_date = datetime.now().date()

        # 查询需求： 当前下订单的所有用户
        # 主表是用户
        # 从表是订单
        # 已知条件是订单日期

        # 一种思路： 从表入手
        # orders = OrderInfo.objects.filter(create_time__gte=cur_date)
        # user_list = []
        # for temp in orders:
        #     # temp指的是订单的模型类对象
        #     user_list.append(temp.user)
        # # user_list存储了所有用户
        # return Response({
        #     "count": len(set(user_list)),
        #     "date": cur_date.strftime("%Y-%m-%d")
        # })

        # 另外一种思路：从主表入手
        user_queryset = User.objects.filter(orders__create_time__gte=cur_date)

        return Response({
            "count": len(user_queryset),
            "date": cur_date.strftime("%Y-%m-%d")
        })

from pytz import timezone
from django.conf import settings

class UserMonthCountView(APIView):
    # 指定管理员权限
    permission_classes = [IsAdminUser]

    def get(self, request):
        cur_date = datetime.now().today() # datetime.now(tz=timezone(settings.TIME_ZONE)).date()
        start_date = cur_date - timedelta(days=29)

        user_list = []
        for index in range(30):
            calc_date = start_date + timedelta(days=index)

            # calc_date当天多少用户注册
            user_quertset = User.objects.filter(date_joined__gte=calc_date,
                                                date_joined__lt=calc_date+timedelta(days=1))
            user_list.append({
                "count": user_quertset.count(),
                "date": calc_date.date()
            })

        return Response(user_list)

from goods.models import GoodsVisitCount
from rest_framework import serializers

class GoodsDaySerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    # category = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = GoodsVisitCount
        fields = ("category", "count")

class GoodsDayView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = GoodsDaySerializer
    queryset = GoodsVisitCount.objects.filter(date=datetime.now().today())


# class GoodsDayView(GenericAPIView):
#     permission_classes = [IsAdminUser]
#     serializer_class = GoodsDaySerializer
#     queryset = GoodsVisitCount.objects.filter(date=datetime.now().today())
#     def get(self, request):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)


# class GoodsDayView(APIView):
#     permission_classes = [IsAdminUser]
#     def get(self, request):
#         cur_date = date(2019,5,10)
#         goods_visit_queryset = GoodsVisitCount.objects.filter(date=cur_date)
#         goods_visit_serializer = GoodsDaySerializer(goods_visit_queryset, many=True)
#         return Response(goods_visit_serializer.data)



from .serializers import JSONWebTokenSerializer
class JSONWebTokenAPIView(GenericAPIView):
    serializer_class = JSONWebTokenSerializer

    # API定义部分
    # POST
    # 127.0.0.1:8000/meiduo_admin/authorizations/
    # 参数：username、password --> json或者表单格式
    # 返回的数据
    # {
    #     "username":xxx
    #     "user_id":xxx,
    #     "token":xxx
    # }
    def post(self, request):
        # 前端传来的用户名和密码在哪？ -->  request.data

        # 构建一个序列化器
        s = self.get_serializer(data=request.data)

        if s.is_valid():
            user = s.validated_data['user']
            token = s.validated_data['token']
            return Response(data={
                "username": user.username,
                "user_id": user.id,
                "token": token
            })

        # 调用数据校验函数
        # # ------1-----
        # s.is_valid(raise_exception=True)
        # 用户校验成功并且token构建成功
        # return Response(data=s.data, status=HTTP_200_OK)

