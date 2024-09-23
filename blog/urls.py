from django.urls import path
from blog.views.task import TaskLisCreateView, TaskDetailView
from blog.views.statistik import UserTaskStatisticView
from blog.views.update_task import CompleteTaskView

urlpatterns = [
    path('tasks/', TaskLisCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('user-task-statistics/', UserTaskStatisticView.as_view(), name='user_task_statistics'),
    path('complete-task/<int:task_id>/', CompleteTaskView.as_view(), name='complete_task'),
]
