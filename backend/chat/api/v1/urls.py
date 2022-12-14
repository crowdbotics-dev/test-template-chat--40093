
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ForwardedMessageViewSet,MessageViewSet,MessageActionViewSet,ThreadViewSet,ThreadActionViewSet,ThreadMemberViewSet
router = DefaultRouter()
router.register('forwardedmessage', ForwardedMessageViewSet )
router.register('message', MessageViewSet )
router.register('threadmember', ThreadMemberViewSet )
router.register('thread', ThreadViewSet )
router.register('threadaction', ThreadActionViewSet )
router.register('messageaction', MessageActionViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
