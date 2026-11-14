# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        #if user submitted the form data
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save() #save the new user to database

            Profile.objects.create(user=user)#create profile for user

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login') #send straight login page
    else:
        #if arriving look at page
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(
        user=request.user
    )


    if request.method == 'POST':

        u_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )

        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(
                request,
                'Profile updated!'
            )

            return redirect('profile')

    else:

        u_form = UserUpdateForm(
            instance=request.user
        )

        p_form = ProfileUpdateForm(
            instance=request.user.profile
        )

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(
        request,
        'users/profile.html',
        context
    )
