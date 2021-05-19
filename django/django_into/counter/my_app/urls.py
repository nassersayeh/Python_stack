from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('destroy/', views.delete),
    path('addtow/', views.addtow),
    path('userinput', views.userinput)
]