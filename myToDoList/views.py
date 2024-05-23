from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView,FormView,ListView,DetailView,DeleteView,UpdateView
from myToDoList.forms import TaskCreate
from myToDoList.models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class TaskCreateView(LoginRequiredMixin,CreateView):
    login_url = "login_user"
    model = Task
    form_class = TaskCreate
    template_name = "myToDoList/creation.html"
    success_url = reverse_lazy('liste')
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)
    
       



class TaskList(LoginRequiredMixin,ListView):
    login_url = "login_user"
    context_object_name = "taches"
    model = Task
    template_name= "myToDoList/liste.html"

    def get_queryset(self):
        self.queryset = Task.objects.filter(user_id = self.request.user.pk)
        return super().get_queryset()


class TaskDetail(LoginRequiredMixin,DetailView):
    login_url = "login_user"
    model = Task
    template_name = "myToDoList/details.html"
    
    
    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        slug = self.kwargs['slug']
        user = self.request.user
        return get_object_or_404(Task,user=user, slug=slug)
        


class TaskDeleteView(LoginRequiredMixin,DeleteView):
    login_url = "login_user"
    model = Task
    template_name = "myToDoList/delete.html"
    success_url = reverse_lazy ("liste")
    
    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        slug = self.kwargs['slug']
        user = self.request.user
        return get_object_or_404(Task,user=user, slug=slug)

    
    

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    login_url = "login_user"
    model = Task
    template_name = "myToDoList/update.html"
    form_class = TaskCreate
    success_url = reverse_lazy ("liste")
    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        slug = self.kwargs['slug']
        user = self.request.user
        return get_object_or_404(Task,user=user, slug=slug)
    
    

class handleTask(FormView):
    form_class = TaskCreate
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        TaskCreate.cleaned_data.user = request.user.pk
        return super().post(request, *args, **kwargs)

