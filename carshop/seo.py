# -*- coding:utf-8 -*-

from rollyourown import seo

class CarShopMetadata(seo.Metadata):
    title = seo.Tag(head=True, max_length=68)
    description = seo.MetaTag(max_length=155)
    keywords = seo.KeywordTag()
    #heading = seo.Tag(name="h1")

    #class Meta:
        #seo_models = ('product', )
        #seo_views = ('product', 'carshop')
    #    pass
