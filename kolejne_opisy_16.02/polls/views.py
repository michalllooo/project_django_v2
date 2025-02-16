from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import CityVote, UserVote
import json

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def dashboard(request):
    city_votes = CityVote.objects.all()
    votes = {city_vote.city_name: city_vote.votes for city_vote in city_votes}
    return render(request, 'dashboard.html', {'votes': votes})

def o_nas(request):
    return render(request, 'o_nas.html')

def region_view(request, region_id):
    template_name = f'wojw/region_{region_id}.html'
   
    return render(request, template_name)

@login_required
def vote_city(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            city_name = data.get('city_name')
            user_vote, created = UserVote.objects.get_or_create(user=request.user)

            if user_vote.city_vote:
                return JsonResponse({'error': 'You have already voted'}, status=400)

            city_vote, created = CityVote.objects.get_or_create(city_name=city_name)
            city_vote.votes += 1
            city_vote.save()

            user_vote.city_vote = city_vote
            user_vote.save()

            return JsonResponse({'votes': city_vote.votes})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=400)