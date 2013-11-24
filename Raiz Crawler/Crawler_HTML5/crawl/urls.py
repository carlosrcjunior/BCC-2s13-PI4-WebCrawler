__author__ = 'Wagner'
from django.conf.urls import patterns,include,url
from django.views.generic import ListView
from models import pesquisa

urlpatterns = patterns('',
                       url(r'^',ListView.as_view(
                           queryset = pesquisa.objects.all().order_by("-date")[:10],
                           template_name = "template\crawl.html")),

                       )