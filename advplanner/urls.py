from django.urls import path
from . import views


urlpatterns = [
    path("", views.adv_index, name="adv_index")
]
