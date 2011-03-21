# coding: utf-8

from django.core.cache import cache
from carshop.system.models import Language

def getAllLanguages():
	languages = cache.get('languages')
	if languages == None:
		languages = Language.objects.all().order_by('language_sequence')
		cache.set('languages', languages)
	return languages

def getLanguage(language_code=None, language_sequence=None):
	languages = getAllLanguages()
	for language in languages:
		if language.language_code == language_code:
			return language
		if language.language_sequence == language_sequence:
			return language
	return None
			