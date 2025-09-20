from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Candidate, Vote

def home(request):
    return render(request, 'voting_app/home.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Registration successful! Please login.")
            return redirect('login')  # redirect to login after successful registration
    return render(request, 'voting_app/register.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('vote')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'voting_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Candidate, Vote

@login_required
def vote(request):
    # Check if the user already voted
    if Vote.objects.filter(voter=request.user).exists():
        return render(request, 'voting_app/vote.html', {
            'already_voted': True,
            'candidates': Candidate.objects.all()
        })

    candidates = Candidate.objects.all()

    if request.method == "POST":
        candidate_id = request.POST.get('candidate')
        if candidate_id:
            candidate = Candidate.objects.get(id=candidate_id)
            # Ensure the user hasn't voted already (extra safety)
            if not Vote.objects.filter(voter=request.user).exists():
                Vote.objects.create(voter=request.user, candidate=candidate)
                messages.success(request, f"You successfully voted for {candidate.name} ({candidate.party})!")
                return redirect('results')
            else:
                messages.error(request, "You have already voted!")
        else:
            messages.error(request, "Please select a candidate before voting.")

    return render(request, 'voting_app/vote.html', {'candidates': candidates, 'already_voted': False})


@login_required
def results(request):
    candidates = Candidate.objects.all()
    for candidate in candidates:
        candidate.vote_count = Vote.objects.filter(candidate=candidate).count()
    return render(request, 'voting_app/results.html', {'candidates': candidates})
