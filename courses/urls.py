from django.urls import path, include
from . import views

urlpatterns = [
    path('discipline/', views.DisciplineListView.as_view()),
    path('discipline/<int:pk>', views.DisciplineDetailView.as_view()),
]
