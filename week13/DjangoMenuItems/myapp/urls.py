from django.urls import path
from myapp import views

urlpatterns=[
    path("", views.navbar,name="navbar"),
]