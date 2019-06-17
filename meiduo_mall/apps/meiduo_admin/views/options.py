
from .mymodels import *

class OptionsSerializer(serializers.ModelSerializer):
    spec = serializers.StringRelatedField(read_only=True)
    spec_id = serializers.IntegerField()
    class Meta:
        model = SpecificationOption
        fields = [
            "id",
            "value",
            "spec",
            "spec_id"
        ]


class OptionsView(ModelViewSet):
    queryset = SpecificationOption.objects.all()
    serializer_class = OptionsSerializer
    pagination_class = MyPage


class OptionSpecSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SPUSpecification
        fields = [
            'id',
            'name'
        ]

class OptionSpecSimple(ModelViewSet):
    queryset = SPUSpecification.objects.all()
    serializer_class = OptionSpecSimpleSerializer