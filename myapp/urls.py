from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('about/', views.about),
    path('hello2/<str:username>', views.hello2),
    path('project/', views.projects),
    path('task/<int:id>', views.tasks),
]