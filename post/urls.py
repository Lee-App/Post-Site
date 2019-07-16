from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.PostListView.as_view(), name='post_list'),
    path('<post_id>/', views.PostDetailView.as_view(), name='post_detail'),
]
