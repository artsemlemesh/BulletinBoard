from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, confirmation, register


app_name='bboard'
urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_add'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_edit'),
    path('register/', register, name='register'),
    path('confirm/<str:confirmation_code>/', confirmation, name='confirm'),
]