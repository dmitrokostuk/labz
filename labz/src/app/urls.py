from django.conf.urls import url
from django.contrib import admin
"""
from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
]__author__ = 'dmitro'
"""
from .views import (list,
                    history,
                    student_create,
                    teacher_create)

urlpatterns = [

    url(r'^$', list, name='list'),
    url(r'^history/$', history, name='history'),
    url(r'^create_student/$', student_create),
    url(r'^teacher_create/$', teacher_create),
   ]