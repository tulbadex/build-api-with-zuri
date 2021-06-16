from django.urls import path
from . import views

urlpatterns = [
    path('create-user/', views.userCreate.as_view(), name='account-create'),
]