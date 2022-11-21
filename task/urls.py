from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from . import views

app_name = 'task'

urlpatterns = [
    path(
        'api/create/',
        views.TaskViewSet.as_view({
            'post': 'create'
        }),
        name='create'
    ),
    path(
        'api/get/<int:pk>/',
        views.TaskViewSet.as_view({
            'get': 'retrieve'
        }),
        name='read'
    ),
    path(
        'api/update/<int:pk>/',
        views.TaskViewSet.as_view({
            'patch': 'partial_update'
        }),
        name='update'
    ),
    path(
        'api/delete/<int:pk>/',
        views.TaskViewSet.as_view({
            'post': 'destroy'
        }),
        name='delete'
    ),
    path(
        'api/list/',
        views.TaskViewSet.as_view({
            'get': 'list',
        }),
        name='list'
    ),
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'api/token/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'
    ),
]
