from django.urls import path

from . import views

app_name = 'task'

urlpatterns = [
    path(
        'api/create/',
        views.TaskCreateView.as_view(),
        name='create'
    ),
    path(
        'api/update/<int:id>/',
        views.TaskUpdateView.as_view(),
        name='update'
    ),
    path(
        'api/list/',
        views.ListTaskView.as_view(),
        name='list'
    ),
]
