from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('webcam')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'index.html')



def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # replace 'home' with the name of your desired homepage URL pattern
        else:
            # handle invalid login
            context = {'error_message': 'Invalid username or password.'}
            return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            confirm_password = form.cleaned_data['password2']
            if password == confirm_password:
                user.set_password(password)
                user.save()
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect( 'tutorial:webcam')
            else:
                # handle password mismatch error
                error_message = 'Password and confirm password do not match.'
                context = {'form': form, 'error_message': error_message}
                return render(request, 'index.html', context)
        else:
            # handle invalid form error
            error_message = 'Invalid form submission.'
            context = {'form': form, 'error_message': error_message}
            return render(request, 'index.html', context)
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'index.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home:index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
