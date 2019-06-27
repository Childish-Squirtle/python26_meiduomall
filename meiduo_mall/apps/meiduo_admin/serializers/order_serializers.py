from rest_framework import serializers
from orders.models import OrderInfo, OrderGoods
from goods.models import SKU


class OrderSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = [
            'order_id',
            'create_time',
            'status',
        ]

        # extra_kwargs = {
        #     1"order_id": {"required": False}
        #     "order_id": {"read_only": True},
        #     "status": {"required": True}
        # }


class SKUSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = [
            'name',
            'default_image'
        ]

class OrderGoodsSerializer(serializers.ModelSerializer):
    #代表的是与当前订单商品表关联的sku商品表 单一的对象
    sku = SKUSimpleSerializer(read_only=True)
    class Meta:
        model = OrderGoods
        fields = ['count', 'price', 'sku']

class OrderDetailSerializer(serializers.ModelSerializer):
    #代表的是当前订单对象，与之关联的所有订单商品表对象（多个）
    skus = OrderGoodsSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()
    class Meta:
        model = OrderInfo
        fields = "__all__"
