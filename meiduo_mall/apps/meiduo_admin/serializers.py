
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from users.models import User
from goods.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "mobile",
            "email",
            "password"
        ]

        extra_kwargs = {
            "password": {
                "write_only": True,
                "max_length": 10,
                "min_length": 8
            },
            "username": {
                "max_length": 10,
                "min_length": 5
            },
            "id": {
                "read_only": True
            }
        }


    def create(self, validated_data):

        # validated_data['password'] = make_password(validated_data['password'])
        # return self.Meta.model.objects.create(**validated_data)
        return self.Meta.model.objects.create_superuser(**validated_data)

class SKUSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKUSpecification
        fields = [
            "spec_id",
            "option_id"
        ]

class SKUSerializer(serializers.ModelSerializer):
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField()
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.IntegerField()

    specs = SKUSpecificationSerializer(read_only=True, many=True)

    class Meta:
        model = SKU
        fields = "__all__"



class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class SPUSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField(read_only=True)
    brand_id = serializers.IntegerField()
    category1_id = serializers.IntegerField()
    category2_id = serializers.IntegerField()
    category3_id = serializers.IntegerField()

    class Meta:
        model = SPU
        exclude = [
            "category1",
            "category2",
            "category3"
        ]



class SPUSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SPU
        fields = [
            "id",
            "name"
        ]


class SPUSepcOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificationOption
        fields = [
            "id",
            "value"
        ]


class SPUSpecSerializer(serializers.ModelSerializer):
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField(read_only=True)

    options = SPUSepcOptionSerializer(read_only=True, many=True)

    class Meta:
        model = SPUSpecification
        fields = "__all__"

class BrandsSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            "id",
            "name"
        ]


class SPUBrandsSerizliser(serializers.ModelSerializer):
    """
        SPU表品牌序列化器
    """
    class Meta:
        model = Brand
        fields = "__all__"


class CategorysSerizliser(serializers.ModelSerializer):
    """
        SPU表分类信息获取序列化器
    """
    class Meta:
        model=GoodsCategory
        fields="__all__"
