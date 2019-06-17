from rest_framework.generics import *
from rest_framework.viewsets import *
from goods.models import SPUSpecification
from rest_framework import serializers
from meiduo_admin.pages import MyPage

class SPUSpecificationSerializer(serializers.ModelSerializer):
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField()
    class Meta:
        model = SPUSpecification
        fields = [
            "id",
            "name",
            "spu",
            "spu_id"
        ]



class SPUSpecificationView(ModelViewSet):
    queryset = SPUSpecification.objects.all()
    serializer_class = SPUSpecificationSerializer
    pagination_class = MyPage

