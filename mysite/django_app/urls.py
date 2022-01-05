from django.urls import path

from . import views

urlpatterns = [
    path('', views.testapi, name='testapi'),
    path('Books', views.Books, name='Books'),
    # path('', views.test, name='test')
]
