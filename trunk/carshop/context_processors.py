# coding: utf-8
import logging
from django.core.cache import cache

from .models import Parameter
from .cache_util import *
from .product.models import Product
from .cart.models import Cart
from .order.models import Order
from .customer.models import Customer

logger = logging.getLogger(__name__)

def getLeftNavigate(request):
    language = request.LANGUAGE_CODE.upper()
    leftNavigate = cache.get('LEFT_NAVIGATE_' + language)
    if leftNavigate == None: # 无指定语言类型菜单缓存则进行数据库加载
        languageObj = getLanguage(language_code=language)
        if not languageObj:
            languageObj = getLanguage(language_sequence=1)
            if not languageObj:
                logger.info('======语言未初始化')
                return {}

        firstMenu = Parameter.objects.filter(parameter_code='product_category', parameter_is_valid=1,
                                             parameter_language=languageObj.id).order_by('parameter_sequence')
        if not firstMenu:
            logger.info('======无 ' + language + ' 纵向菜单项,返回默认菜单')
            leftNavigate = cache.get('LEFT_NAVIGATE_' + getLanguage(language_sequence=1).parameter_value)
            if not leftNavigate:
                return {}
            else:
                return {'leftNavigate': leftNavigate}

        leftNavigate = []
        for menuItem in firstMenu:
            item = {'firstMenu': menuItem}
            #secondMenu = Product.objects.filter(product_category=menuItem.id)

            #if not secondMenu == None:
            #	item['secondMenu'] = secondMenu
            leftNavigate.append(item)

        cache.set('LEFT_NAVIGATE_' + language, leftNavigate)
    return {'leftNavigate': leftNavigate}


def getTopNavigate(request):
    language = request.LANGUAGE_CODE.upper()
    topNavigate = cache.get('TOP_NAVIGATE_' + language)
    if not topNavigate:
        languageObj = getLanguage(language_code=language)
        if not languageObj:
            languageObj = getLanguage(language_sequence=1)
            if not languageObj:
                logger.info('======语言未初始化')
                return {}

        topNavigate = Parameter.objects.filter(parameter_code='top_navigate', parameter_is_valid=1,
                                               parameter_language=languageObj.id).order_by('parameter_sequence')
        if not topNavigate:
            logger.info('======无 ' + language + ' 菜单项,返回默认菜单')
            topNavigate = cache.get('TOP_NAVIGATE_' + getLanguage(language_sequence=1).parameter_value)
            if not topNavigate:
                return {}
            else:
                return {'topNavigate': topNavigate}
        else:
            cache.set('TOP_NAVIGATE_' + language, topNavigate)

    return {'topNavigate': topNavigate}

    
def getCartCount(request):
    cart = Cart.objects.get_or_create_from_request(request)
    cart_count = cart.cart_count

    if cart_count is not None:
        return {'cart_count': cart_count}
    else:
        return {}

def getUnPalCount(request):

    if request.user.is_authenticated():
        order_status__count = Order.objects.calc_unpal_count(request)
        if 0 == order_status__count:
                return {}
        return {'order_status__count': order_status__count}
    else:
        return {}
    
    
    
    
    
    
    
    
