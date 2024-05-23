from django.urls import path
from myToDoList.views import TaskCreateView, TaskDeleteView, TaskDetail, TaskList, TaskUpdateView, handleTask



urlpatterns = [
    path("liste/", TaskList.as_view(), name="liste"),
    path("create/", TaskCreateView.as_view(), name="create"),
    path("", TaskCreateView.as_view(), name="create"),
    path("details/<slug:slug>/", TaskDetail.as_view(), name="details"),
    path("update/<slug:slug>/", TaskUpdateView.as_view(), name="update"),
    path("delete-task/<slug:slug>/", TaskDeleteView.as_view(), name="delete-task"),
    
    #path("handleTask/", handleTask.as_view())
    
]
