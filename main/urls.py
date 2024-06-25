from django.urls import path
from .views import indexview,dehashview
urlpatterns = [
    path('',indexview,name='index'),
    path('dehash',dehashview,name='dehash')
]
