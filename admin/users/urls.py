from django.urls import path
from .views import ProfileInfoAPIView, ProfilePasswordAPIView, register, login, AuthenticatedUser, logout, PermissionAPIView, RoleViewSet, UserGenericAPIView


urlpatterns = [

    path('register/', register, name='register'),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('user/', AuthenticatedUser.as_view(), name='user'),
    path("permissions/", PermissionAPIView.as_view(), name='permissions'),
    path('roles/', RoleViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('roles/<str:pk>/', RoleViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('users/info/', ProfileInfoAPIView.as_view()),
    path('users/password/', ProfilePasswordAPIView.as_view()),
    path('users/', UserGenericAPIView.as_view()),
    path('users/<str:pk>/', UserGenericAPIView.as_view()),
]
