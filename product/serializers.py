from rest_framework import serializers
from product.models import Product, Category, Review
from rest_framework.exceptions import ValidationError


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ' id title description price category'.split()


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = " id name product_list product_count".split()


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text product stars product_title'.split()


class RatingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title rating'


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, min_length=4)


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(required=False, default='No description')
    price = serializers.FloatField()
    category_id = serializers.IntegerField()

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category not found.')
        return category_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=700)
    product_id = serializers.IntegerField()
    stars = serializers.IntegerField(required=False, min_value=1, max_value=5)

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except  Product.DoesNotExist:
            raise ValidationError('Your product is not found.')
        return product_id
