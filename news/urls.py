from django.urls import path
from .views import *

urlpatterns = [
   path('', Index, name = 'Index'),
   path('Channels', Channels, name = 'Channels'),
   path('Country', Country, name = 'Country'),
   path('Category', Category, name = 'Category'),
   path('Keyword', Keyword, name = 'Keyword'),
   path('Search', Search, name = 'Search'),
   path('Bbc', Bbc, name = 'Bbc'),
   path('Abc', Abc, name = 'Abc'),
   path('Alj', Alj, name = 'Alj'),
   path('Hindu', Hindu, name = 'Hindu'),
   path('Fox', Fox, name = 'Fox'),
   path('Tech', Tech, name = 'Tech'),
   path('Google', Google, name = 'Google')
]
