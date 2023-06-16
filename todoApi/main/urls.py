from django.urls import path
from .views import tasks_create_list_view, task_detail_view, TaskListCreateAPIView, TaskDetailAPIView, TaskDetailView, \
    TaskListCreateView

urlpatterns = [
    path('tasks/', tasks_create_list_view),  # GET/ POST
    path('task/<int:pk>/', task_detail_view),  # GET / PUT PATCH / DELETE

    #generics
    path('class/tasks/', TaskListCreateView.as_view()),
    path('class/tasks/<int:pk>/', TaskDetailView.as_view()),

      # apiview
#     path('class/tasks/', TaskListCreateAPIView.as_view()),
#     path('class/tasks/<int:pk>/', TaskDetailAPIView.as_view()),
 ]

# 127.0.0.1:8000/api/v1/tasks/ -> GET/POST tasks_create_list_view
# 127.0.0.1:8000/api/v1/tasks/id/ -> GET/PUT/PATCH/DELETE tasks_detail_view
