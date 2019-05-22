from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testApp.forms import SignupForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_view(request):
    return render(request,'testApp/home.html')

@login_required
def java_view(request):
    return render(request,'testApp/java.html')

@login_required
def python_view(request):
    return render(request,'testApp/python.html')

@login_required
def aptitude_view(request):
    return render(request,'testApp/aptitude.html')

def logout_view(request):
    return render(request,'testApp/logout.html')

def signup_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request,'testApp/signup.html',{'form':form})
