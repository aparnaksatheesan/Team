from django.shortcuts import render
from .models import football, Team


# Create your views here.
def index(request):
    object1 = football.objects.all()
    object2 = Team.objects.all()
    return render(request, 'index.html', {'result': object1, 'team': object2})
