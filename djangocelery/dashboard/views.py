from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .tasks import background_html_to_pdf_task


def home(request):

    data = User.objects.all()
    context = {
        'data': data
    }
    return render(request, 'dashboard/index.html', context=context)


def process_pdf(request):

    user_id = request.user.id

    background_html_to_pdf_task.delay(user_id)

    return redirect('dashboard')