from django.urls import path 
from .import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("add_todo", views.add_todo, name= "add_todo"),
    path("update/<str:pk>", views.update, name= "update"),
    path("delete/<str:pk>", views.delete, name= "delete"),
]
