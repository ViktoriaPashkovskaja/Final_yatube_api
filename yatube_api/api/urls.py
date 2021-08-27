from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView, TokenVerifyView

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')
router.register('follow', FollowViewSet,
                basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('vi/jwt/create', TokenObtainPairView.as_view(), name="jwt_create"),
    path("vi/jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("vi/jwt/verify/", TokenVerifyView.as_view(), name="jwt_verify")
]
