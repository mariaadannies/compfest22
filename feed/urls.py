from django.urls import path
from .views import HomePageView, AddPostView, DeletePostView, HomePageViewDesccendingView

app_name = 'feed'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('post/', AddPostView.as_view(), name='post'),
    path('buy/1/', DeletePostView.as_view(), name='buy'),
    path('latest/', HomePageViewDesccendingView.as_view(), name='view_descending'),
    # path('balance/', BalanceBoxView.asView(), name='balance_box')
    # path('buy/<id>/', views.DeletePostView, name='buy'),
]