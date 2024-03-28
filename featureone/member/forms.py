from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.forms import forms
from django.forms import widgets

def Register(request):
    if request.method == "POST" :
        form = UserCreationForm()
        if form.is_valid():
            form.save()
    else :
        form = UserCreationForm()
        context = {'form' : form}
        return render(request, 'member/login.html', context = context)
    
    
    
    
    
    
    