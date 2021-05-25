from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
    
def signup(request):
    #template = 'registration/signup.html'
    #context = {'form':form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('polls:home')
    else:
        form = UserCreationForm()
    
    return render(request,'registration/signup.html',{'form':form})