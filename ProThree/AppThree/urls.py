from django.conf.urls import url
from AppThree import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^other$', views.otherFunc, name='other')
]
