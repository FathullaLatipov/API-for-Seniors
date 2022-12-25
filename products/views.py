from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .models import ImagesModel, MapModel, PriceListModel, UserWishlistModel
from rest_framework.decorators import parser_classes, api_view

from products.helpers import modify_input_for_multiple_files
from products.models import CategoryModel, HouseModel, AmenitiesModel, HouseImageModel
from products.serializers import CategorySerializer, AmenitiesSerializer, \
    HomeDetailSerializer, HomeFavSerializer, HomeImageSerializer, \
    WebAmenitiesSerializer, WebPriceSerializer, NewWebHomeCreateSerializer, \
    PriceListSerializer, NewAllWebHomeCreateSerializer, UserWishlistModelSerializer, \
    GetUserWishlistModelSerializer
from products.utils import get_wishlist_data


class CategoryListAPIView(generics.ListAPIView):
    ''' Categories '''
    queryset = CategoryModel.objects.order_by('pk')
    serializer_class = CategorySerializer


class AmenitiesListAPIView(generics.ListAPIView):
    ''' Удобства (Amenities in product)'''
    queryset = AmenitiesModel.objects.order_by('pk')
    serializer_class = AmenitiesSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 1000


# web

class WebPriceListAPIView(generics.ListAPIView):
    queryset = PriceListModel.objects.order_by('-pk')
    serializer_class = WebPriceSerializer
    pagination_class = StandardResultsSetPagination



# web WebHomeSerializer
class WebHouseListAPIView(generics.ListAPIView):
    ''' Products (Houses)'''
    queryset = HouseModel.objects.filter(draft=False)
    serializer_class = NewWebHomeCreateSerializer


# web create Home
class WebHomeListAPIView(ListAPIView):
    queryset = HouseModel.objects.all()
    serializer_class = NewAllWebHomeCreateSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['product_status', 'object', 'building_type', 'number_of_rooms',
                        'type', 'rental_type']

    search_fields = ['web_address_title']
    ordering_fields = ['price', 'created_at']


class SearchWebHomeListAPIView(ListAPIView):
    queryset = HouseModel.objects.all()
    serializer_class = NewAllWebHomeCreateSerializer
    filter_backends = [SearchFilter]
    search_fields = ['web_address_title']


class WebHomeCreateView(mixins.CreateModelMixin, GenericViewSet):
    queryset = HouseModel.objects.all()
    serializer_class = NewWebHomeCreateSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated, ]

# web
@api_view(['GET', 'POST'])
def snippet_list(request):
    if request.method == 'GET':
        snippets = HouseModel.objects.all()
        serializer = NewWebHomeCreateSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NewWebHomeCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class HouseFavListAPIView(generics.ListAPIView):
    ''' Fav (Houses)'''
    queryset = HouseModel.objects.order_by('pk')
    serializer_class = HomeFavSerializer


class HouseDetailAPIView(APIView):
    def get(self, request, pk):
        houses = HouseModel.objects.get(id=pk)
        houses.view_count += 1
        houses.save()
        serializer = NewAllWebHomeCreateSerializer(houses, context={'request': request}, )
        return Response(serializer.data)


class WishlistHouseDetailAPIView(mixins.UpdateModelMixin, GenericViewSet):
    queryset = HouseModel.objects.all()
    serializer_class = NewWebHomeCreateSerializer

    def update(self, request, *args, **kwargs):
        user_profile = self.get_object()
        serializer = self.get_serializer(user_profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class HouseAddCreateAPIView(generics.CreateAPIView):
    queryset = HouseModel.objects.all()
    serializer_class = NewWebHomeCreateSerializer
    pagination_class = StandardResultsSetPagination
    search_fields = ['title', 'description']

    def get_serializer_context(self):
        return {'request': self.request}



class HouseUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = HouseModel.objects.all()
    serializer_class = NewWebHomeCreateSerializer

    def update(self, request, *args, **kwargs):
        user_profile = self.get_object()
        serializer = self.get_serializer(user_profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class HouseDestroyAPIView(mixins.DestroyModelMixin, GenericViewSet):
    queryset = HouseModel.objects.all()
    serializer_class = NewWebHomeCreateSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserWishlistModelView(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin, GenericViewSet):
    queryset = UserWishlistModel.objects.all()
    serializer_class = UserWishlistModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']


class GetHouseFavListAPIView(generics.ListAPIView):
    ''' Fav (Houses)'''
    queryset = UserWishlistModel.objects.order_by('pk')
    serializer_class = GetUserWishlistModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']


class RandomHouseModelAPIView(generics.ListAPIView):
    queryset = HouseModel.objects.order_by('?')
    serializer_class = NewWebHomeCreateSerializer

