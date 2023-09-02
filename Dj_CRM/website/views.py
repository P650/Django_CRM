from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpform
from .models import Record

#username: admin
#password: pavan123


# Create your views here.
def home(request):
    # check if they login
    # print(request.method)
    records = Record.objects.all()
    #it ll load all the records from the database

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
        return render(request, 'home.html', {'records':records})


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


def record_details(request, pk):
    if request.user.is_authenticated:
        #looking for the record with the id of pk
        cus_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'cus_record':cus_record})

    else:
        messages.success(request, "Please login to view the record")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        cus_record = Record.objects.get(id=pk)
        cus_record.delete()
        messages.success(request, "You have successfully deleted the record")
        return redirect('home')

    else:
        messages.success(request, "Please login to delete the record")
        return redirect('home')