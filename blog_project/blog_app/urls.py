# blog_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)   # Registering the PostViewSet
router.register(r'comments', CommentViewSet)  # Registering the CommentViewSet

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
]
