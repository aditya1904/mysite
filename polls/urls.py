from django.conf.urls import url

from . import views
app_name = 'polls'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^users/$', views.UserView.as_view(), name='user'),
	url(r'^users/(?P<pk>[0-9]+)/detail/$', views.UserDetailView.as_view(), name='userdetail'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),	
	url(r'^accounts/register/$', views.SignUpView.as_view(), name='signup'),
	url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
	url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout'),
]
