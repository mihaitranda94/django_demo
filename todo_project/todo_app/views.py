from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from todo_app.models import ToDoList, ToDoItem

# Create your views here.


def home(request):
    return HttpResponse("Home sweet home :)")


class ListListView(ListView):
    model = ToDoList
    template_name = "todo_app/index.html"


class ItemListView(ListListView):
    model = ToDoItem
    template_name = "todo_app/todo_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context


def list_list_view(request):
    todo_lists = ToDoList.objects.all()  # Fetch all ToDoList objects
    return render(request, "todo_app/index.html", {"object_list": todo_lists})
