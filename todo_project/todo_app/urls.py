from django.urls import path
from .views import ListListView, ItemListView


urlpatterns = [
    path(route="", view=ListListView.as_view(), name="index"),
    path(route="list/<int:list_id>/", view=ItemListView.as_view(), name="list"),
]
