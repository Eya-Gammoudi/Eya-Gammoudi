from django.shortcuts import render, redirect
import json
from .forms import collectorForm, collectorLoginForm
from .models import collector
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.
def collectorSignup(request):
    if request.method == 'POST':
        form = collectorForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['FirstName']
            last_name = form.cleaned_data['LastName']
            email = form.cleaned_data['Email']
            password = make_password(form.cleaned_data['password'])
            phone_number = form.cleaned_data['PhoneNumber']
            location = form.cleaned_data['Location']          
             
            # Create an instance of the Greener model and save it
            greener_instance = collector.objects.create(
                FirstName=first_name,
                LastName=last_name,
                Email=email,
                password=password,
                PhoneNumber=phone_number,
                Location=location
            )
            return redirect('/')  # Redirect to some page after successful signup
        else:
            msg = 'Form is not valid'
    else:
        form = collectorForm()

    return render(request, 'collector_signup.html', {'form': form})



def collectorLogin(request):
    if request.method == 'POST':
        form = collectorLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                if user.is_approved:  # Vérification si l'utilisateur est approuvé
                    login(request, user)
                    messages.success(request, 'You have successfully logged in.')
                    return redirect('/')  # Redirection vers la page d'accueil après une connexion réussie
                else:
                    messages.error(request, 'Your account has not been approved by the administrator.')
            else:
                messages.error(request, 'Invalid email or password.')

            remember_me = request.POST.get('remember')
            if remember_me:
                request.session.set_expiry(604800)  # Une semaine
            else:
                request.session.set_expiry(0)  # Session du navigateur
    else:
        form = collectorLoginForm()

    return render(request, 'collector_login.html', {'form': form})