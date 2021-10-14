from django.urls import path
from positivafront import views

urlpatterns = [
    path ('',views.home,name="Home")
]
