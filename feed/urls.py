from django.urls import path
from .views import HomePageView, AddPostView, DeletePostView, HomePageViewDesccendingView, BalanceBoxView

app_name = 'feed'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('post/', AddPostView.as_view(), name='post'),
    path('buy/1/', DeletePostView.as_view(), name='buy'),
    path('latest/', HomePageViewDesccendingView.as_view(), name='view_descending'),
    path('balance/', BalanceBoxView.as_view(), name='balance_box'),
]