from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import RegisterForm, ProfileForm


def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if register_form.is_valid() and profile_form.is_valid():
            register_form.save()

            user = User.objects.get(email=register_form.cleaned_data.get('email'))
            
            user_profile = UserProfile.objects.create(user=user, website=profile_form.cleaned_data.get('website'), car=profile_form.cleaned_data.get('car'))
            user_profile.save()

            return redirect('user-register')
    else:
        register_form = RegisterForm()
        profile_form = ProfileForm()

    context = {
        'register_form': register_form,
        'profile_form': profile_form
    }
    return render(request, 'users/register.html', context=context)
