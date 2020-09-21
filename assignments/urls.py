from django.urls import path, include
from . import views

urlpatterns = [

    path('assignment/create', views.AssignmentCreateView.as_view()),

]
