# -*- coding:utf-8 -*-
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType

CART_OBJ = 'CART-OBJ'

class CartManager(models.Manager):

    def get_from_request(self, request):
        try:
            cart = self.get(pk=request.session.get(CART_OBJ))
            if cart.user is None and request.user.is_authenticated():
                cart.user = request.user
                cart.session = request.session.session_key
                cart.save()
        except Cart.DoesNotExist, e:
            # log
            return None
        except Exception, e:
            print e
        else:
            return cart


    def get_or_create_from_request(self, request):
        try:
            cart = self.get_from_request(request)
            if cart is None:
                user = request.user if request.user.is_authenticated() else None
                cart = self.create(session=request.session.session_key, user=user)
                request.session[CART_OBJ] = cart.pk
        except Exception, e:
            print e
        else:
            return cart

class Cart(models.Model):
    session = models.CharField(max_length=40, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    creation_date = models.DateTimeField(verbose_name=_('creation date'), default=datetime.datetime.now())
    checked_out = models.BooleanField(default=False, verbose_name=_('checked out'))
    
    objects = CartManager()

    def put_into_cart(self, product, quantity):
        CartItem.objects.add_item(self, product, quantity)

    def put_out_cart(self, item_id):
        CartItem.objects.remote_item(self, item_id)

    def show_cart_items(self):
        return CartItem.objects.filter(cart=self)

    def clean_cart(self):
        CartItem.objects.extra(where=['cart_id=' + str(self.pk),]).delete()

    @property
    def total_price(self):
        cartItem = CartItem.objects.filter(cart=self)
        total_price = 0
        if cartItem is not None:
            for item in cartItem:
                total_price = total_price + item.total_price
            
        return total_price
    class Meta:
        db_table = 'cart'
        ordering = ('-creation_date',)

    def __unicode__(self):
        return unicode(self.creation_date)




class ItemManager(models.Manager):
    #def get(self, *args, **kwargs):
    #    if 'product' in kwargs:
    #        kwargs['content_type'] = ContentType.objects.get_for_model(type(kwargs['product']))
    #        kwargs['object_id'] = kwargs['product'].pk
    #        kwargs['object_name'] = kwargs['product'].product_name
    #        kwargs['unit_price'] = kwargs['product_price'].product_name
    #        del(kwargs['product'])
    #    return super(ItemManager, self).get(*args, **kwargs)

    def create(self, **kwargs):
        if 'product' in kwargs:
            kwargs['object_id'] = kwargs['product'].pk
            kwargs['object_name'] = kwargs['product'].product_name
            kwargs['unit_price'] = str(kwargs['product'].product_price)
        return super(ItemManager, self).create(**kwargs)

    def add_item(self, cart, product, quantity):
        try:
            cartItem = self.get(object_id=product.pk)
        except CartItem.DoesNotExist, e:
            self.create(cart=cart, product=product, quantity=quantity)
        else:
            cartItem.quantity = cartItem.quantity + int(quantity)
            cartItem.save()


    def remote_item(self, cart, item_id):
        try:
            cartItem = self.get(pk=item_id, cart=cart)
        except CartItem.DoesNotExist, e:
            raise CartItem.DoesNotExist()
        else:
            cartItem.delete()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, verbose_name=_('cart'))
    quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
    unit_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=_('unit price'))
    # product as generic relation
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    object_name = models.CharField(max_length=100)

    objects = ItemManager()

    class Meta:
        db_table = 'cart_item'
        ordering = ('cart',)

    def __unicode__(self):
        return u''

    @property
    def total_price(self):
        return self.quantity * self.unit_price

#    total_price = property(total_price)

    # product
    def get_product(self):
        return self.content_type.get_object_for_this_type(id=self.object_id)

    def set_product(self, product):
        self.content_type = ContentType.objects.get_for_model(type(product))
        self.object_id = product.pk
        self.object_name = product.product_name

    product = property(get_product, set_product)

