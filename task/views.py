from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return super().get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["example"] = 'this is in context now'
        return context

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
        id = kwargs.get('pk')
        task = get_object_or_404(Task, id=id)
        task.delete()
        return super().destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        id = kwargs.get('pk')

        task = self.get_queryset().get(id=id)
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
