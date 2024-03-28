from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def login(request):
    return render(request, "member/login.html")
def logout(request):
    pass
def register(request):
    pass
def dashboard(request):
    pass