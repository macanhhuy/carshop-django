# coding: utf-8

from django.core.cache import cache
from carshop.models import Parameter

def getAllLanguages():
    languages = cache.get('languages')
    if languages == None:
        languages = Parameter.objects.filter(parameter_code='language', parameter_is_valid='1').order_by(
            'parameter_sequence')
        cache.set('languages', languages)
    return languages


def getLanguage(language_code=None, language_sequence=None):
    languages = getAllLanguages()
    for language in languages:
        if language.parameter_value == language_code:
            return language
        if language.parameter_sequence == language_sequence:
            return language
    return None
			