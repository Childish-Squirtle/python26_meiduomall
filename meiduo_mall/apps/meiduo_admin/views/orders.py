
from .mymodels import *

class OrderInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = [
            'order_id',
            'create_time'
        ]



class OrdersView(ModelViewSet):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderInfoSerializer
    pagination_class = MyPage



class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = [
            'name',
            'default_image'
        ]


class OrderSKUSerializer(serializers.ModelSerializer):
    sku = SKUSerializer(read_only=True)
    class Meta:
        model = OrderGoods
        fields = [
            'count',
            'price',
            'sku',
        ]


class OrderInfoDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    skus = OrderSKUSerializer(read_only=True, many=True)
    class Meta:
        model = OrderInfo
        fields = [
            'order_id',
            'user',
            'total_count',
            'total_amount',
            'freight',
            'pay_method',
            'skus',
            'status',
            'create_time'
        ]
        extra_kwargs = {
            "order_id": {
                "required": False,
            },
            "freight": {
                "required": False,
            },
            "total_amount": {
                "required": False,
            }
        }


class OrdersDetailView(RetrieveAPIView, UpdateAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderInfoDetailSerializer
    lookup_field = 'order_id'
