# voter/urls.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.conf.urls import url

from . import views_admin

urlpatterns = [
    url(r'^$', views_admin.voter_list_view, name='voter_list',),
    url(r'^edit_process/$', views_admin.voter_edit_process_view, name='candidate_edit_process'),
    url(r'^(?P<voter_id>[0-9]+)/edit/$', views_admin.voter_edit_view, name='voter_edit'),
    url(r'^(?P<voter_id>[0-9]+)/summary/$', views_admin.voter_summary_view, name='voter_summary'),
]
