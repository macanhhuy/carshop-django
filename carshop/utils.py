#-*- coding:utf-8

from django.forms.util import ErrorList

class NoStyleErrorList(ErrorList):
    def __unicode__(self):
        return self.no_style()

    def no_style(self):
        return u'%s' % ''.join([u'%s' % e for e in self])
	
