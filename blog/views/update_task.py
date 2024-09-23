from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from blog.models import Task


class CompleteTaskView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id, owner=request.user)
        except Task.DoesNotExist:
            return Response({"error": "Задача не найдена"}, status=status.HTTP_404_NOT_FOUND)

        task.status = True
        task.save()

        return Response({
            'message': 'Статус задачи успешно обновлён на "выполнено".',
            'task_id': task.id,
            'status': task.status
        }, status=status.HTTP_200_OK)
