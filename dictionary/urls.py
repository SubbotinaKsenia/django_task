from django.conf.urls import url
from . import views

app_name = 'dictionary'

urlpatterns = [
    url(r'^define/$', views.define),
]