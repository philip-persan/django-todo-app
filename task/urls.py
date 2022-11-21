from django.urls import path

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
]
