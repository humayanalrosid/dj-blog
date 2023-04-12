from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogUploadForm, SignUpForm, LoginForm
from django.contrib import messages
from .models import Blog
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'app/home.html', {'blogs':blogs})

def add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = BlogUploadForm(request.POST, request.FILES)
            
            if form.is_valid():
                blog = form.save(commit=False)
                blog.user = request.user
                blog.save()
                messages.success(request, 'Blog added successfully.')
                return redirect('home')
        else:
            form = BlogUploadForm()
        return render(request, 'app/add.html', {'form':form})
    else:
        messages.warning(request, 'You need to login.')
        return redirect('login')        

def blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'app/blog.html', {'blog': blog})

def update(request, slug):
    if request.user.is_authenticated:
        blog = get_object_or_404(Blog, slug=slug)
        
        if request.method == "POST":
            form = BlogUploadForm(request.POST, request.FILES, instance=blog)
            
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                messages.success(request, 'Blog updated successfully.')
                return redirect('home')
        else:
            form = BlogUploadForm(instance=blog)
        return render(request, 'app/update.html', {'form':form})
    else:
        messages.warning(request, 'You need to login.')
        return redirect('login')


def delete(request, slug):
    if request.user.is_authenticated:
        blog = get_object_or_404(Blog, slug=slug)
        blog.delete()
        messages.warning(request, 'Blog deleted succesfully.')
        return redirect('home')
    else:
        messages.warning(request, 'You must login.')
        return redirect('login')   

# User Authentication
def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully.')
                return redirect('login')
            else:
                messages.warning(request, 'Something went wrong.')
                return redirect('signup') 
        else:
            form = SignUpForm() 
        return render(request, 'app/signup.html', {'form': form})
    else:
        messages.warning(request, 'You are already logged in.')
        return redirect('home')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                
                user = authenticate(username=uname, password=upass)
                if user is not None:  
                    login(request, user)
                    messages.success(request, 'Account created successfully.')
                    return redirect('home')
            else:
                messages.warning(request, 'Something went wrong.')
                return redirect('login')  
        else:
            form = LoginForm() 
        return render(request, 'app/login.html', {'form': form})

    else:
        messages.warning(request, 'You are already logged in.')
        return redirect('home')

def user_logout(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'You need to login.')
        return redirect('login')
    else:
        logout(request)
        messages.warning(request, 'Logged out successfullt..')
        return redirect('home')

