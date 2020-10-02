from django.urls import path

from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('<int:anupam_id>',views.details,name="details")
    
]