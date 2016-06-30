from django.conf.urls import url


from . import views
app_name = 'calci'
urlpatterns = [ 
	url('^$', views.index, name='index'),
]
