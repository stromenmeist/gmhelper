from django.urls import path
from . import views


urlpatterns = [
    path("", views.adv_index, name="adv_index"),
    path("index", views.adv_index, name="adv_index"),
    path("detail/<pk>", views.adv_detail, name="adv_detail"),
]
