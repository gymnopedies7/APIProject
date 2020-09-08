from django.urls import path
import Prediction.views as views

urlpatterns = [
    path('add/', views.api_add, name = 'api_add')
]