# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        #if user submitted the form data
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() #save the new user to database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login') #send straight login page
    else:
        #if arriving look at page
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})
