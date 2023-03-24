from django.shortcuts import render
from .forms import  LoginForm

#sign__in view
def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
    