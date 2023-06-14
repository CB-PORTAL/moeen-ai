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
from .views import user_detail, ai_model_detail, create_ai_model, index, submit_feedback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/<int:user_id>/', user_detail),
    path('ai_model/<int:ai_model_id>/', ai_model_detail),
    path('create_ai_model/', create_ai_model),
    path('index/', index),
    path('submit_feedback/', submit_feedback),
]