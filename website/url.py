from django.conf.urls import url
from django.contrib import admin

from django.views.generic import TemplateView
from .views import (
    rank,
    home,
    rules,
    contact,
)

urlpatterns = [
	# url(r'^$', Timeline,name="Timeline"),
	# url(r'related/(?P<Topic>[^/]+)$',RelatedTimeline, name='RelatedTimeline'),
	url(r'rank$',rank, name='rank'),
    url(r'^$',home,name='home'),
    url(r'^rules$',rules,name='rules'),
    url(r'^contact$',contact,name='contact'),
	# url(r'^rank$', rank,name="ranks"),
	# url(r'^$',index,name="index"),

	]
