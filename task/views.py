from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskSerializer


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
