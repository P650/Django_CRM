from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpform

#username: admin
#password: pavan123


# Create your views here.
def home(request):
    # check if they login
    print(request.method)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #authemticate
        user = authenticate(request, username=username, password=password)
        print("user", user)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return redirect('home')
        else:
            messages.success(request, "Error logging in Please login again")
            return redirect('home')

    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpform(request.POST)
        if form.is_valid():
            form.save()
            #authenticate them
            username = form.cleaned_data['username'] 
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect('home')

    else:
        form = SignUpform()
        return render (request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})
