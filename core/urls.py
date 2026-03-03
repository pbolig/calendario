from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, EventViewSet, StickyNoteViewSet, CalendarViewSet, RegisterView, UserInfoView, LoginView, LogoutView

router = DefaultRouter()
router.register(r'calendars', CalendarViewSet, basename='calendar')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'events', EventViewSet, basename='event')
router.register(r'stickynotes', StickyNoteViewSet, basename='stickynote')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('auth/login/', LoginView.as_view(), name='auth_login'),
    path('auth/logout/', LogoutView.as_view(), name='auth_logout'),
    path('auth/user/', UserInfoView.as_view(), name='auth_user'),
    path('', include(router.urls)),
]
