from django.shortcuts import render
from django.contrib.auth.models import User

def home(request):

    data = User.objects.all()
    context = {
        'data': data
    }
    return render(request, 'dashboard/index.html', context=context)