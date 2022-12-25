from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from rest_framework.decorators import action

from products.models import CategoryModel, HouseModel, AmenitiesModel, MapModel, HouseImageModel, ImagesModel, \
    NewHouseImages, PriceListModel, HowSaleModel, UserWishlistModel
from user.models import CustomUser


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'title', 'subtitle', 'image', 'created_at']


class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmenitiesModel
        fields = ['id', 'title', 'image', 'created_at']


# web
class WebAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmenitiesModel
        fields = ['id', 'title', 'image', 'created_at']


class WebPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceListModel
        fields = ['id', 'price_t']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapModel
        exclude = ['created_at']


class HomeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseImageModel
        fields = ['property_id', 'image']

    def get_img_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.image.url)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewHouseImages
        fields = ['images']

    def get_img_url(self, obj):
        return self.context['request'].build_absolute_url(obj.image.url)


class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceListModel
        fields = ['price_t']


class NewWebHowSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowSaleModel
        fields = ['title']


class HouseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseModel
        fields = ['type']


class HouseRentalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseModel
        fields = ['rental_type']


# web
class NewAllWebHomeCreateSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )
    amenities = WebAmenitiesSerializer(many=True)
    price_type = PriceListSerializer()
    how_sale = NewWebHowSaleSerializer()
    type = HouseTypeSerializer
    rental_type = HouseRentalTypeSerializer

    # address = AddressSerializer()

    class Meta:
        model = HouseModel
        fields = ['id', 'creator', 'title', 'descriptions', 'price', 'price_type',
                  'type', 'rental_type', 'property_type', 'object',
                  'web_address_title', 'web_address_latitude', 'web_address_longtitude',
                  'pm_general', 'pm_residential', 'images', 'uploaded_images',
                  'number_of_rooms', 'floor', 'floor_from', 'building_type',
                  'app_ipoteka', 'app_mebel', 'app_new_building',
                  'amenities', 'phone_number', 'how_sale',
                  'isBookmarked', 'draft', 'product_status', 'view_count', 'created_at',
                  ]


class NewWebHomeCreateSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )
    how_sale = NewWebHowSaleSerializer

    # address = AddressSerializer()

    class Meta:
        model = HouseModel
        fields = ['id', 'creator', 'title', 'descriptions', 'price', 'price_type',
                  'type', 'rental_type', 'property_type', 'object',
                  'web_address_title', 'web_address_latitude', 'web_address_longtitude',
                  'pm_general', 'pm_residential', 'images', 'uploaded_images',
                  'number_of_rooms', 'floor', 'floor_from', 'building_type',
                  'app_ipoteka', 'app_mebel', 'app_new_building',
                  'amenities', 'phone_number', 'how_sale',
                  'isBookmarked', 'draft', 'created_at',
                  ]
        extra_kwargs = {"creator": {"read_only": True}, "product_status": {"read_only": True}}

    def create(self, validated_data):
        title = validated_data.get('title')
        descriptions = validated_data.get('descriptions')
        price = validated_data.get('price')
        price_types = validated_data.pop('price_type')
        type = validated_data.get('type')
        how_sale = validated_data.get('how_sale')
        rental_type = validated_data.get('rental_type')
        property_type = validated_data.get('property_type')
        object = validated_data.get('object')
        web_address_title = validated_data.get('web_address_title')
        web_address_latitude = validated_data.get('web_address_latitude')
        web_address_longtitude = validated_data.get('web_address_longtitude')
        pm_general = validated_data.get('pm_general')
        pm_residential = validated_data.get('pm_residential')
        pm_kitchen = validated_data.get('pm_kitchen')
        number_of_rooms = validated_data.get('number_of_rooms')
        floor = validated_data.get('floor')
        floor_from = validated_data.get('floor_from')
        building_type = validated_data.get('building_type')
        app_ipoteka = validated_data.get('app_ipoteka')
        app_mebel = validated_data.get('app_mebel')
        app_new_building = validated_data.get('app_new_building')
        amenities = validated_data.get('amenities')
        phone_number = validated_data.get('phone_number')
        draft = validated_data.get('draft')
        isBookmarked = validated_data.get('isBookmarked')
        uploaded_data = validated_data.pop('uploaded_images')
        creator = self.context['request'].user
        print(creator, 'this is creator')
        titles = [i.title for i in amenities]
        amenities_titles = AmenitiesModel.objects.filter(title__in=titles)
        price_t = PriceListModel.objects.get(price_t=price_types)
        target_objs = HouseModel.objects.create(price_type=price_t, creator=creator,
                                                title=title, price=price,
                                                how_sale=how_sale,
                                                web_address_title=web_address_title,
                                                phone_number=phone_number,
                                                web_address_latitude=web_address_latitude,
                                                web_address_longtitude=web_address_longtitude,
                                                type=type,
                                                draft=draft,
                                                isBookmarked=isBookmarked,
                                                rental_type=rental_type,
                                                object=object,
                                                descriptions=descriptions,
                                                property_type=property_type,
                                                pm_general=pm_general,
                                                pm_residential=pm_residential,
                                                pm_kitchen=pm_kitchen,
                                                number_of_rooms=number_of_rooms,
                                                floor=floor,
                                                floor_from=floor_from,
                                                building_type=building_type,
                                                app_ipoteka=app_ipoteka,
                                                app_mebel=app_mebel,
                                                app_new_building=app_new_building,
                                                )
        target_objs.amenities.add(*amenities_titles)
        # if creator in validated_data:
        # target_objs.creator.add(*creator)
        for uploaded_item in uploaded_data:
            new_product_image = NewHouseImages.objects.create(product=target_objs, images=uploaded_item)
        return target_objs

    def get_img_url(self, obj):
        urls = []
        for i in obj.images.all():
            myurl = self.context['request'].build_absolute_uri(i.image.url)
            urls.append(myurl)
        return urls


class HomeFavSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = HouseModel
        fields = ['id', 'title', 'price', 'address', 'isBookmarked', 'created_at']


class HomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['title']


class HomeDetailSerializer(serializers.ModelSerializer):
    category = HomeCategorySerializer()
    address = AddressSerializer()
    # image = HomeImageSerializer(many=True)
    amenities = AmenitiesSerializer(many=True)

    # choices = serializers.SerializerMethodField('get_choices')

    class Meta:
        model = HouseModel
        fields = '__all__'


class UserWishlistModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWishlistModel
        fields = '__all__'


class GetUserWishlistModelSerializer(serializers.ModelSerializer):
    user = CustomUser()
    product = NewAllWebHomeCreateSerializer()

    class Meta:
        model = UserWishlistModel
        fields = '__all__'
