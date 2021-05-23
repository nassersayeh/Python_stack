from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('adddojo',views.AddDojo),
    path('addninja', views.AddNinja),
    path('delete',views.delete)
]