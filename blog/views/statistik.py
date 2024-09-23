from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from blog.models import Task


class UserTaskStatisticView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        total_tasks = Task.objects.filter(owner=user).count()

        completed_tasks = Task.objects.filter(owner=user, status=True).count()
        pending_tasks = Task.objects.filter(owner=user, status=False).count()

        return Response(
            {'total_tasks': total_tasks, 'completed_tasks': completed_tasks, 'pending_tasks': pending_tasks})
