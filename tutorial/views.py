from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def webcam(request):
    return render(request, 'webcam.html')