from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('addbook',views.addbook),
    path('books/<int:id>',views.view),
    path('books/<int:id>/addauthortobook', views.addauthor),
    path('addauthors',views.addauthors),
    path('addauthorsform',views.addauthorsform),
    path('addauthors/<int:id>',views.show),
    path('addauthors/<int:id>/addbookauthor',views.addbooks)
]