# -*- coding:utf-8

from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.forms.widgets import RadioFieldRenderer

class NonStyleRadioFieldRenderer(RadioFieldRenderer):

	def render(self):
		return mark_safe(u'%s' % u'\n'.join([u'%s' % force_unicode(w) for w in self]))
