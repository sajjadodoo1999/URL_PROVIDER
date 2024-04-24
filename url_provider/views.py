from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, request
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.


def login_function(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to the home page after successful login
            else:
                messages.error(request, 'Invalid username or password.')
        return render(request, 'url_services/login_new.html')

@login_required(login_url='login')
def dashboard(request):
    all_description = UserDescription.objects.filter(username=request.user.username).order_by('-id')
    print(all_description)
    context = {
        'all_description':all_description,
    }
    return render(request, 'url_services/dashboard.html',context)

@login_required(login_url='login')
def logout_function(request):
    logout(request)
    return redirect('login')

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            print("Successful")
            return redirect("login")
    context = {'form': form}

    return render(request, 'url_services/register_new.html', context)

@login_required(login_url='login')
def add_description(request):
    if request.method == "POST":
        username = request.POST['user_hidden']
        title = request.POST['title']
        description = request.POST['description']
        UserDescription.objects.create(username=username,title=title,description=description).save()
        return redirect('dashboard')
    context = {
        'edit': False,
        'user' : request.user
    }
    return render(request, 'url_services/add_description.html',context)


def status(request,pk):
    latest_description = UserDescription.objects.filter(username=pk).order_by('-id').first()
    if latest_description:
        context = {
            'latest_description':latest_description,
            'latest_description_username':latest_description.username.title()
        }
        return render(request, 'url_services/status_description.html',context)
    return HttpResponse('NO SUCH USERNAME EXIST IN SYSTEM')
@login_required(login_url='login')
def edit_description(request,pk):
    if request.method == "POST" and request.POST['edit']:
        print(request.POST)
        title_id = request.POST['title_id']
        title = request.POST['title']
        description = request.POST['description']
        record = UserDescription.objects.get(id=int(title_id))
        if record:
            record.title = title
            record.description = description
            record.save()
            return redirect('dashboard')
    all_description = UserDescription.objects.get(id=int(pk))
    context = {
        'user' : request.user,
        'all_description' : all_description,
        'edit':True
    }
    return render(request, 'url_services/add_description.html',context)


@login_required(login_url='login')
def delete_description(request,pk):
    description = UserDescription.objects.get(id=int(pk))
    if description:
        description.delete()
    return redirect('dashboard')

