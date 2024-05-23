from django.shortcuts import render, redirect
from .forms import  WasteRequestForm, greenerForm, greenerLoginForm
from .models import greener
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import WasteRequest



# Create your views here.
def greenerhome(request):
    return render(request, 'greener_home.html')



def greenerSignup(request):
    if request.method == 'POST':
        form = greenerForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['FirstName']
            last_name = form.cleaned_data['LastName']
            email = form.cleaned_data['Email']
            password = make_password(form.cleaned_data['password'])
            phone_number = form.cleaned_data['PhoneNumber']
            location = form.cleaned_data['Location']          
             
            # Create an instance of the Greener model and save it
            greener_instance = greener.objects.create(
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
        form = greenerForm()

    return render(request, 'greener_signup.html', {'form': form})



def greenerLogin(request):
    if request.method == 'POST':
        form = greenerLoginForm(request.POST)
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
        form = greenerLoginForm()

    return render(request, 'greener_login.html', {'form': form})



def create_waste_request(request):
    if request.method == 'POST':
        form = WasteRequestForm(request.POST)
        if form.is_valid():
            waste_request = form.save(commit=False)
            waste_request.greener = request.user  # Associating current user with the request
            waste_request.save()
            messages.success(request, 'Your waste request has been submitted successfully.')
            return redirect('greenerHome')
        else:
            messages.error(request, 'Form is not valid. Please correct the errors.')
    else:
        form = WasteRequestForm()

    return render(request, 'waste_request.html', {'form': form})
