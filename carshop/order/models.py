# -*- coding:utf-8 -*-

#from django.contrib.auth.models import User
import datetime
from django.db.models import Count
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..product.models import Product
from ..models import Parameter, AddressFormat
from ..customer.models import Customer
from ..db.models import *
from ..cart.models import Cart

class OrderManager(models.Manager):
    def merge_order(self, orders):
        pass

    def create_from_cart(self, request, cart=None, **kwargs):
        if cart is not None:
            try:
                cart_items = cart.cart_items
                if len(cart_items) > 0:
                    order = self.create(**kwargs)
                    OrderProduct.objects.add_or_update_order_products(order, cart_items)

                    cart.clean_cart(request)
                else:
                    return None
            except Exception, e:
                print e
                return None
            else:
                return order
        else:
            return None

    def get_order_and_order_products(self, customer=None, order_status=1, page_index=1, page_size=5):
        try:
            order_list = self.filter(customer=customer, order_status=order_status)
            paginator = Paginator(order_list, page_size)

            try:
                orders = paginator.page(page_index)
            except PageNotAnInteger:
                orders = paginator.page(1)
            except EmptyPage:
                orders = paginator.page(paginator.num_pages)

        except Order.DoesNotExist:
            return None
        else:
            for order in orders.object_list:
                try:
                    orderProducts = OrderProduct.objects.filter(order=order)
                except OrderProduct.DoesNotExist:
                    setattr(order, 'order_products', None)
                else:
                    setattr(order, 'order_products', orderProducts)
                    for orderProduct in orderProducts:
                        setattr(orderProduct, 'product_image', orderProduct.product.product_image)
            return orders

    def calc_unpal_count(self, request):
        try:
            order_status__count = Order.objects.filter(customer = request.user.get_profile(), order_status=1).aggregate(Count('order_status'))['order_status__count']
        except Order.DoesNotExist:
            return 0
        except Customer.DoesNotExist:
            return 0
        else:
            return order_status__count

class Order(models.Model): # 订单表

    STATUS_CHOICES = (
    (u'1', u'unpaid'),
    (u'2', u'paid'),
    (u'3', u'delivery'),
    (u'4', u'confirmed'),
    (u'5', u'over'),
    )

    id = UUIDField(primary_key=True, editable=False)
    customer = models.ForeignKey(Customer) # 客户ID

    #cart = models.OneToOneField(Cart)

    #    customer_name = models.CharField(max_length=64) # 客户名(接收人)
    #    customer_company = models.CharField(max_length=64, blank=True, null=True) # 客户公司
    #    customer_street_address = models.CharField(max_length=64, blank=True, null=True) # 客户街道地址
    #    customer_suburb = models.CharField(max_length=32, blank=True, null=True) # 客户住宅区
    #    customer_city = models.CharField(max_length=32, blank=True, null=True) # 客户城市
    #    customer_postcode = models.CharField(max_length=10, blank=True, null=True) # 客户邮编
    #    customer_state = models.CharField(max_length=32, blank=True, null=True) # 客户所在州
    #    customer_country = models.CharField(max_length=32, blank=True, null=True) # 客户国家
    #    customer_telephone = models.CharField(max_length=32, blank=True, null=True) # 客户电话
    #    customer_email_address = models.CharField(max_length=96, blank=True, null=True) # 客户EMAIL
    #    customer_address_format = models.ForeignKey(AddressFormat, related_name='customer_address_format', blank=True, null=True) # 客户地址格式

    #    delivery_name = models.CharField(max_length=64, blank=True, null=True) # 送货人名
    #    delivery_company = models.CharField(max_length=64, blank=True, null=True) # 送货公司
    #    delivery_street_address = models.CharField(max_length=64, blank=True, null=True) # 送货(人/公司？)街道地址
    #    delivery_suburb = models.CharField(max_length=32, blank=True, null=True) # 送货(人/公司?)所在区
    #    delivery_city = models.CharField(max_length=32, blank=True, null=True) # 送货
    #    delivery_postcode = models.CharField(max_length=10, blank=True, null=True) #
    #    delivery_state = models.CharField(max_length=32, blank=True, null=True) #
    #    delivery_country = models.CharField(max_length=32, blank=True, null=True) #
    #    delivery_address_format = models.ForeignKey(AddressFormat, related_name='delivery_address_format', blank=True, null=True) #

    billing_first_name = models.CharField(max_length=30) #
    billing_last_name = models.CharField(max_length=30) #
    billing_company = models.CharField(max_length=64, blank=True, null=True) #
    billing_street_address = models.TextField(max_length=500, blank=True, null=True) #
    billing_suburb = models.CharField(max_length=32, blank=True, null=True) #
    billing_city = models.CharField(max_length=32, blank=True, null=True) #
    billing_postcode = models.CharField(max_length=10, blank=True, null=True) #
    billing_state = models.CharField(max_length=32, blank=True, null=True) #
    billing_country = models.CharField(max_length=32, blank=True, null=True) #
    billing_address_format = models.ForeignKey(AddressFormat, related_name='billing_address_format', blank=True,
                                               null=True) #

    payment_method = models.CharField(max_length=128, blank=True, null=True) # 付款方式
    payment_module_code = models.CharField(max_length=32, blank=True, null=True) # ？
    shipping_method = models.CharField(max_length=128, blank=True, null=True) # 购买方式
    shipping_module_code = models.CharField(max_length=32, blank=True, null=True) #

    #coupon_code
    time_purchased = models.DateTimeField(blank=True, null=True) # 购置时间

    order_total_price = models.DecimalField(max_digits=10, decimal_places=2) # 总价格
    currency = models.CharField(max_length=3, blank=True, null=True) # ?
    #paypal_ipn
    ip_address = models.CharField(max_length=96) # 下单IP
    order_status = models.CharField(max_length=2, choices=STATUS_CHOICES) # 订单状态

    objects = OrderManager()

    def save(self, force_insert=False, force_update=False, using=None):
        try:
            self.time_purchased = datetime.datetime.now()
        except:
            pass
        super(Order, self).save(force_insert, force_update, using)

    class Meta:
        db_table = "order"


class OrderProductManager(models.Manager):
    def add_or_update_order_products(self, order, items):
        orderProducts = self.filter(order=order)

        for item in items:
            if len(orderProducts) != 0:
                for orderProduct in orderProducts:
                    if item.product_id == orderProduct.product_id and item.quantity != orderProduct.product_quantity:
                        orderProduct.product_quantity = item.quantity
                        orderProduct.save()
                        break

            else:
                self.create(order=order, product_id=item.product_id, product_name=item.product.product_name,
                            product_quantity=item.quantity, product_unit_price=item.product.product_price,
                            product_final_price=item.product.product_price)


    def add_order_products(self, order, items):
        for item in items:
            self.create(order=order, product_id=item.product_id, product_name=item.product.product_name,
                        product_quantity=item.quantity, product_unit_price=item.product.product_price,
                        product_final_price=item.product.product_price)

    def add_order_product(self, order, item):
        self.create(order=order, product_id=item.product_id, product_name=item.product.product_name,
                    product_quantity=item.quantity, product_unit_price=item.product.product_price,
                    product_final_price=item.product.product_price)

    def remove_order_product(self):
        pass


class OrderProduct(models.Model): # 订单项表
    order = models.ForeignKey(Order) # 订单ID
    product = models.ForeignKey(Product) # 产品ID
    product_name = models.CharField(max_length=64)
    product_quantity = models.IntegerField() # 产品数量
    product_unit_price = models.DecimalField(max_digits=10, decimal_places=2) # 产品单价
    product_final_price = models.DecimalField(max_digits=10, decimal_places=2) # 产品最终单价
    product_tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) # 产品税
    #product_image = models.ImageField(u'产品图片', upload_to='product_images', blank=True, null=True)
    onetime_charge = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) # 一次性付款数目？

    #product_is_free # 是否免费
    #product_discount = models.ForeignKey(Discount) # 优惠券ID
    product_prid = models.CharField(max_length=36, blank=True, null=True) #

    objects = OrderProductManager()

    class Meta:
        db_table = "order_product"

#class OrderProductAttribute(models.Model)

class OrderProductDownload(models.Model): # 订单下载表
    order = models.ForeignKey(Order) # 订单ID
    order_product = models.ForeignKey(OrderProduct) # 订单产品ID
    order_product_filename = models.CharField(max_length=255) # 文件名
    download_maxdays = models.IntegerField() # 最大下载时间(天)
    download_count = models.IntegerField() # 最大下载次数

    class Meta:
        db_table = "order_product_download"

        #product_prid = models


class OrderStatus(models.Model): # 订单状态表
    order = models.ForeignKey(Order) # 订单ID
    order_status = models.ForeignKey(Parameter, related_name='order_status') # 订单状态
    time_status = models.DateTimeField(default=datetime.datetime.now) # 添加时间
    time_pass = models.DateTimeField() # 确认时间
    order_pass_use = models.ForeignKey(Customer, related_name="manager_user", blank=True, null=True) # 确认管理人
    order_send_type = models.ForeignKey(Parameter, related_name='order_send_type', blank=True, null=True) # 发送状态

    class Meta:
        db_table = "order_status"


class OrderStatusHistory(models.Model): # 订单状态历史表
    order = models.ForeignKey(Order) # 订单ID
    status = models.ForeignKey(Parameter) # 订单状态
    time_added = models.DateTimeField(default=datetime.datetime.now) # 添加时间
    #customer_notified
    comment = models.TextField(blank=True, null=True) # 注释

    class Meta:
        db_table = "order_status_history"

#class OrderTotal(models.Model):

#class Paypal(models.Model):
	
	
	
	
	

	

