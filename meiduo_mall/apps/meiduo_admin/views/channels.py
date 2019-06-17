
from .mymodels import *


class GoodsChannelSerializer(serializers.ModelSerializer):
    group = serializers.StringRelatedField(read_only=True)
    group_id = serializers.IntegerField()
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.IntegerField()
    class Meta:
        model = GoodsChannel
        fields = [
            "id",
            'category',
            'category_id',
            'group',
            'group_id',
            'sequence',
            'url',
        ]

class GoodsChannelView(ModelViewSet):
    queryset = GoodsChannel.objects.all()
    serializer_class =GoodsChannelSerializer
    pagination_class = MyPage



class GoodsChannelGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsChannelGroup
        fields = [
            'id',
            "name"
        ]


class GoodsChannelGroupView(ListAPIView):
    queryset = GoodsChannelGroup.objects.all()
    serializer_class = GoodsChannelGroupSerializer

class GoodsChannelCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = [
            "id",
            'name'
        ]

class GoodsChannelCategoriesView(ListAPIView):
    queryset = GoodsCategory.objects.filter(parent=None)
    serializer_class = GoodsChannelCategoriesSerializer