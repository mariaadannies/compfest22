from django.urls import path
from .views import HomePageView, AddPostView

app_name = 'feed'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('post/', AddPostView.as_view(), name='post')
]