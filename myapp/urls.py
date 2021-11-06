from django.urls import path
from myapp.views import index,PostDetail,like_view

app_name = 'myapp'

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:pk>/', PostDetail.as_view(), name = 'postdetail'),
    path('likes/',like_view, name = 'like'),
]
