from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User

from .models import Task
from .serializers import TaskSerializer


class ListTaskView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(instance=tasks, many=True)
        return Response(serializer.data)


class TaskCreateView(APIView):
    def post(self, request):
        data = request.data
        user = User.objects.get(id=data.get("user"))
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
