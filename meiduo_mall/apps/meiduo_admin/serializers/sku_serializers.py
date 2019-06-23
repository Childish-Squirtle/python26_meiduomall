from rest_framework import serializers
from goods.models import SKU, SKUSpecification, GoodsCategory, SPU, SPUSpecification,SpecificationOption


class SKUSpecModelSerializer(serializers.ModelSerializer):
    spec_id = serializers.IntegerField()
    option_id = serializers.IntegerField()
    class Meta:
        model = SKUSpecification
        fields = ['spec_id', 'option_id']


#定义SKU序列化器
class SKUModelSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    spu = serializers.StringRelatedField()
    spu_id = serializers.IntegerField()

    #specs代表的是与sku对象关联的所有的从表数据对象SKUSpecification
    specs = SKUSpecModelSerializer(many=True, read_only=True)

    class Meta:
        model = SKU
        fields = "__all__"

#定义GoodsCategory序列器
class GoodsCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ['id', 'name']

#定义SPU序列化器
class SPUSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SPU
        fields = ['id', 'name']

class SpecOptSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificationOption
        fields = ['id', 'value']

#定义SPUSpecification序列化器
class SPUSpecModelSerializer(serializers.ModelSerializer):
    spu = serializers.StringRelatedField()
    spu_id = serializers.IntegerField()

    #与之关联的所有的从表对象
    options = SpecOptSerializer(many=True, read_only=True)

    class Meta:
        model = SPUSpecification
        fields = ['id', 'name', 'spu', 'spu_id', 'options']