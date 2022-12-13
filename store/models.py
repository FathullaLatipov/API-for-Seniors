from django.db import models
from django.utils.translation import gettext_lazy as _

from products.models import PriceListModel
from user.models import CustomUser


class StoreAmenities(models.Model):
    title = models.CharField(max_length=90, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Store_amenities')
        verbose_name_plural = _('Store_amenities')


class UseForModel(models.Model):
    title = models.CharField(max_length=300, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Для')
        verbose_name_plural = _('Для')


class StoreModel(models.Model):
    creator = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='stores', null=True,
                                blank=True)
    name = models.CharField(max_length=200, verbose_name=_('name'))
    description = models.TextField()
    image = models.ImageField(upload_to='store_images', max_length=100, verbose_name=_('image'), null=True)
    brand_image = models.ImageField(upload_to='avatar_image', verbose_name=_('brand_image'), null=True)
    brand = models.CharField(max_length=200, verbose_name=_('brand'), null=True)
    price = models.PositiveIntegerField(verbose_name=_('price'), null=True)
    price_type = models.ForeignKey(PriceListModel, on_delete=models.CASCADE, related_name='store_price_type', null=True)
    use_for = models.ForeignKey(UseForModel, on_delete=models.CASCADE, null=True)
    phoneNumber = models.PositiveIntegerField(verbose_name=_('phoneNumber'))
    address = models.CharField(max_length=400, verbose_name=_('address'), null=True)
    email = models.EmailField(verbose_name=_('email'))
    isBookmarked = models.BooleanField(default=False, verbose_name=_('isBookmarked'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    draft = models.BooleanField(default=False)
    PRODUCT_STATUS = [
        (0, 'InProgress'),
        (1, 'PUBLISH'),
        (2, 'DELETED'),
        (3, 'ARCHIVED'),
        (4, 'REJECTED')
    ]
    product_status = models.IntegerField(
        choices=PRODUCT_STATUS,
        default=0,
        null=True
    )
    store_amenitites = models.ManyToManyField(StoreAmenities, verbose_name=_('store_amenities'))

    def __str__(self):
        return self.name

    @staticmethod
    def get_from_wishlist(request):
        wishlist = request.session.get('wishlist', [])
        return StoreModel.objects.filter(pk__in=wishlist)

    class Meta:
        verbose_name = _('Обустройствo дома')
        verbose_name_plural = _('Обустройствo дома')
        ordering = ['-id']

# tempaltes, update
# tempaltes, admin