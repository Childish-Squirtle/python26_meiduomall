
from .mymodels import *


class GoodsBrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            "id",
            "name",
            "logo",
            "first_letter"
        ]

class GoodsBrandsView(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = GoodsBrandsSerializer
    pagination_class = MyPage