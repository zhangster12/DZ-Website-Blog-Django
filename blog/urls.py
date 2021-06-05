from .views import BlogPostListView, BlogPostDetailView, BlogPostFeaturedView
from django.urls import path

urlpatterns = [
    path('', BlogPostListView.as_view()),
    path('featured/', BlogPostFeaturedView.as_view()),
    path('<slug>', BlogPostDetailView.as_view()),
]