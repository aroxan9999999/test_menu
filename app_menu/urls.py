from django.urls import path, include
from .views import *

urlpatterns = [
    path('page1', page_1_view, name='page_1'),
    path('page2', page_2_view, name='page_2'),
    path('page3', page_3_view, name='page_3'),
]
