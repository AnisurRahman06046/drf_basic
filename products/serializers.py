from rest_framework import serializers
from . models import Products


# model serializer
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['title','qty','description']


# the below serializer method is raw method to understand the concept. for production we wiil use model serializer which is coded above



# class ProductsSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=75)
#     qty = serializers.IntegerField()
#     description = serializers.CharField()
#     # date = serializers.DateTimeField()
    
#     def create(self,validated_data):
#         return Products.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         # return super().update(instance, validated_data)
#         instance.title = validated_data.get('title',instance.title)
#         instance.qty = validated_data.get('qty',instance.qty)
#         instance.description = validated_data.get('description',instance.description)
#         instance.save()
#         return instance