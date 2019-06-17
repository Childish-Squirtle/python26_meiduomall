
from rest_framework.generics import ListAPIView,GenericAPIView,CreateAPIView,ListCreateAPIView,\
    DestroyAPIView,UpdateAPIView
from users.models import User
from meiduo_admin.serializers import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from goods.models import *
from rest_framework.viewsets import ModelViewSet
from meiduo_admin.pages import MyPage

# GET
# /meiduo_admin/users/?keyword=<搜索内容>&page=<页码>&pagesize=<页容量>



class UserView(ListAPIView, CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = MyPage
