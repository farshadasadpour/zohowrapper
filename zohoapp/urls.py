from django.urls import path

from . import views

urlpatterns = [
    path("", views.ApiZoho.as_view(), name="zohoapi"),
]