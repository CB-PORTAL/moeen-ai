from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User, AIModel, InterfaceLayer, TrainingSession, CursorMovement, TrainingScape, CursorCustomization, Feedback, SessionHistory

# Create your views here.

def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user_detail.html', {'user': user})

def ai_model_detail(request, ai_model_id):
    ai_model = get_object_or_404(AIModel, pk=ai_model_id)
    return render(request, 'ai_model_detail.html', {'ai_model': ai_model})

def create_ai_model(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        # Assuming the currently logged-in user is the creator
        user = request.user
        ai_model = AIModel.objects.create(name=name, description=description, user=user)
        return HttpResponse(f'Success! AI model "{ai_model.name}" created.')
    return render(request, 'create_ai_model.html')

# Additional views for other models can be defined in a similar manner

def index(request):
    # Logic to retrieve data or perform actions
    return render(request, 'index.html')

def submit_feedback(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        rating = int(request.POST['rating'])
        user = request.user
        feedback = Feedback.objects.create(user=user, comment=comment, rating=rating)
        return HttpResponse(f'Thank you for your feedback! Rating: {feedback.rating}')
    return render(request, 'feedback_form.html')

# More views as per your application's requirements