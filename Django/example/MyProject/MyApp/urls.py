from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^hello$', views.Hello, name = "hello"),
	url(r'^hello2$', views.Hello2, name = "hello2"),
	url(r'^hello3$',views.Hello3),
	url(r'^signup$',views.signup, name = "sign up"),
]