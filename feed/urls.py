from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>/', FeedView.as_view({'get': 'retrieve'})),
    path('', FeedView.as_view({'get': 'list'})),
]



