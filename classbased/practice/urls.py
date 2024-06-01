from django.urls import path
from .views import *

urlpatterns = [
    path('asdf/', Myview.as_view(), name='index'),
    path('', GreekCreate.as_view(), name='index'),
]