from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')
def o_nas(request):
    return render(request, 'o_nas.html')
def dashboard(request):
    return render(request, 'dashboard.html')

def region_view(request, region_id):
    template_name = f'wojw/region_{region_id}.html'
    return render(request, template_name, {'region_id': region_id})