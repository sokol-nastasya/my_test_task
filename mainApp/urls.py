from django.conf.urls import url
from mainApp import views

urlpatterns = [
	url(r'^$', views.main, name = 'main'),
	url(r'^about/$', views.about, name = 'about'),
	url(r'^services_lists/(?P<show_main_id>[0-9]+)/$', views.show_singlpages, name = 'show_singlpages'),
	url(r'^keywords/(?P<k_id>[0-9]+)/$', views.keywords, name = 'keywords'),
	url(r'^test/$', views.news, name = 'test'),
	url(r'^news/(?P<news_id>[0-9]+)/$', views.show_news, name = 'news'),
	url(r'^news/addlikes/(?P<news_id>\d+)/$', views.addlikes, name = 'addlikes'),

]
