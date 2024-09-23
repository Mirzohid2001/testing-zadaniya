from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from blog.models import Task
from blog.serializers.task import TaskSerializer
from rest_framework.filters import SearchFilter


class TaskLisCreateView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']

    def get(self, request):
        tasks = Task.objects.filter(owner=request.user)

        search_query = request.query_params.get('search')
        if search_query:
            tasks = tasks.filter(title__icontains=search_query) | tasks.filter(description__icontains=search_query)

        status_filter = request.query_params.get('status')
        if status_filter is not None:
            if status_filter.lower() == 'true':
                status_filter = True
            elif status_filter.lower() == 'false':
                status_filter = False
            else:
                return Response({'error': 'Invalid status filter value'}, status=status.HTTP_400_BAD_REQUEST)

            tasks = tasks.filter(status=status_filter)

        sort_by = request.query_params.get('ordering', 'created_at')
        tasks = tasks.order_by(sort_by)

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Task.objects.get(pk=pk, owner=user)
        except Task.DoesNotExist:
            return None

    def get(self, request, pk):
        task = self.get_object(pk, request.user)
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk, request.user)
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk, request.user)
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
