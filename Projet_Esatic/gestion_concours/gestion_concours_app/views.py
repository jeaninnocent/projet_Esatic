from django.shortcuts import render, redirect
from .forms import CandidatForm

def index(request):
    return render(request, 'gestion_concours_app/index.html')

def concours(request):
    return render(request, 'gestion_concours_app/concours.html')

def contact(request):
    return render(request, 'gestion_concours_app/contact.html')

from .forms import CandidatForm

def inscription(request):
    if request.method == 'POST':
        form = CandidatForm(request.POST, request.FILES)
        if form.is_valid():
            candidat = form.save()
            return render(request, 'gestion_concours_app/recap_inscription.html', {'candidat': candidat})
    else:
        form = CandidatForm()
    return render(request, 'gestion_concours_app/inscription.html', {'form': form})

