from django.urls import include, path
from . import views

app_name = 'dictionary'

urlpatterns = [
    path('define/<str:word>/', views.define),
]
