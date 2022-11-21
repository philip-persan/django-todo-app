from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Task
from .permissions import IsOwnerOrAdmin
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self):
        pk = self.kwargs.get('pk', '')
        obj = get_object_or_404(self.get_queryset(), id=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_permissions(self):
        if self.request.method in ['PATH', 'DELETE']:
            return [IsOwnerOrAdmin(), ]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def destroy(self, request, *args, **kwargs):
        task = self.get_object()
        task.delete()
        return super().destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = TaskSerializer(
            instance=task,
            data=request.data,
            many=False,
            context={'request': request},
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ListTaskView(ListAPIView):
    model = Task
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskCreateView(APIView):
    def post(self, request):
        data = request.data
        user = request.user
        task = Task.objects.create(
            user=user,
            description=data.get("description"),
            completed=data.get("completed")
        )
        serializer = TaskSerializer(instance=task, many=False)
        print(request.data)
        return Response(serializer.data)


class TaskUpdateView(APIView):
    def patch(self, request, id):
        task = Task.objects.get(id=id)
        serializer = TaskSerializer(instance=task, many=False),
        return Response(serializer.data)
