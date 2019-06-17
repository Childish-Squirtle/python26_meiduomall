
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



class SKUView(ModelViewSet):
    queryset = SKU.objects.all()
    serializer_class = SKUSerializer
    pagination_class = MyPage

    def get_queryset(self):
        keyword = self.request.query_params.get("keyword")
        print(keyword)
        if keyword:
            return self.queryset.filter(name__contains=keyword)
        return self.queryset


from django.shortcuts import reverse
class SKUCategorieView(ListAPIView):
    queryset = GoodsCategory.objects.all()
    serializer_class = GoodsCategorySerializer

    def get_queryset(self):
        return self.queryset.filter(parent_id__gt=37)


class SPUSimpleView(ListAPIView):
    queryset = SPU.objects.all()
    serializer_class = SPUSimpleSerializer



class SPUSpecView(ListAPIView):
    queryset = SPUSpecification.objects.all()
    serializer_class = SPUSpecSerializer

    def get_queryset(self):
        spu_id = self.kwargs.get("pk")
        if spu_id:
            return self.queryset.filter(spu_id=spu_id)
        return self.queryset.all()


