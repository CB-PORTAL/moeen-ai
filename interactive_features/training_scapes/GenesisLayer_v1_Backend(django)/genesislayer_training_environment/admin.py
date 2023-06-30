from django.contrib import admin
from .models import User, AIModel, InterfaceLayer, TrainingSession, CursorMovement, TrainingScape, CursorCustomization, Feedback, SessionHistory

# Register your models here.

admin.site.register(User)
admin.site.register(AIModel)
admin.site.register(InterfaceLayer)
admin.site.register(TrainingSession)
admin.site.register(CursorMovement)
admin.site.register(TrainingScape)
admin.site.register(CursorCustomization)
admin.site.register(Feedback)
admin.site.register(SessionHistory)