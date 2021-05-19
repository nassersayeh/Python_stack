from django.urls import path     
from . import views
urlpatterns = [
    path('', views.start),
    path('start', views.index),
    path('reset',views.reset),
    

]