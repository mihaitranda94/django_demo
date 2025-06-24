import datetime
from django.db import models
from django.urls import reverse
from django.utils import timezone
from todo_app.constants import EXTENDED_CHARFIELD_LENGTH, STD_CHARFIELD_LENGTH

# Create your models here.


class ToDoList(models.Model):
    title = models.CharField(max_length=STD_CHARFIELD_LENGTH, verbose_name="List Title", unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title


class ToDoItem(models.Model):
    title = models.CharField(max_length=STD_CHARFIELD_LENGTH, verbose_name="List Item Title")
    description = models.CharField(max_length=EXTENDED_CHARFIELD_LENGTH, verbose_name="List Item Description")
    created_date = models.DateField(auto_now=True)
    due_date = models.DateField(default=datetime.datetime.now() + datetime.timedelta(days=7))
    todo_list = models.ForeignKey(to="ToDoList", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("item-update", args=[str(self.todo_list.id), str(self.id)])

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]
        unique_together = [["title", "todo_list"]]
