
from rest_framework.generics import ListAPIView,GenericAPIView,CreateAPIView,ListCreateAPIView,\
    DestroyAPIView,UpdateAPIView,RetrieveAPIView
from users.models import User
from meiduo_admin.serializers import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from goods.models import *
from rest_framework.viewsets import ModelViewSet
from meiduo_admin.pages import MyPage
from orders.models import *