from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

class AIModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class InterfaceLayer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    layer_settings = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TrainingSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ai_model = models.ForeignKey(AIModel, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)

class CursorMovement(models.Model):
    session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE)
    movement_data = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

class TrainingScape(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interface_layer = models.ForeignKey(InterfaceLayer, on_delete=models.CASCADE)
    ai_model = models.ForeignKey(AIModel, on_delete=models.CASCADE)
    configuration = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CursorCustomization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customization_details = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class SessionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    training_session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE)
    log = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)