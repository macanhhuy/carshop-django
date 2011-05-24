# coding: utf-8
import logging
from django.core.cache import cache
from carshop.models import Parameter
from carshop.cache_util import *
from carshop.product.models import Product

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
