from django.urls import path, include
from .views import *


urlpatterns = [
    path('<int:pk>/', PostListView.as_view()),
    path('post/', PostView.as_view({'post': 'create'})),
    path('post/<int:pk>/', PostView.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})),
    path('comment/', CommentView.as_view({'post': 'create'})),
    path('comment/<int:pk>/', CommentView.as_view({'put': 'update','delete': 'destroy'})),
]

