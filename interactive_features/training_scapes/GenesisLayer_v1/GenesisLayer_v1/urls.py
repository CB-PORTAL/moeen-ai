"""
URL configuration for GenesisLayer_v1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'genesislayer_training_environment'  # the name of your app

urlpatterns = [
    path('', views.index, name='index'),  # URL for the index view

    path('user/<int:user_id>/', views.user_detail, name='user_detail'),  # URL for the user_detail view
    
    path('ai_model/<int:ai_model_id>/', views.ai_model_detail, name='ai_model_detail'),  # URL for the ai_model_detail view
    
    path('create_ai_model/', views.create_ai_model, name='create_ai_model'),  # URL for the create_ai_model view

    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),  # URL for the submit_feedback view
]