
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


class SPUGoodsView(ModelViewSet):
    """
        SPU表的增删改查
    """
    # 指定序列化器
    serializer_class = SPUSerializer
    # 指定查询及
    queryset = SPU.objects.all()
    # 指定分页
    pagination_class = MyPage



class SPUBrandView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = SPUBrandsSerizliser


class ChannelCategorysView(ListAPIView):
    """
            获取spu一级分类
    """
    serializer_class = CategorysSerizliser
    queryset = GoodsCategory.objects.all()  # parent=None表示一级分类信息

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return self.queryset.filter(parent=None)
        return self.queryset.filter(parent_id=pk)