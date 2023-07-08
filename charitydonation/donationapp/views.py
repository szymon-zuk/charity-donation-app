from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import RegistrationForm
from .models import Donation, Institution


class LandingPage(View):
    def get(self, request):
        total_bags = Donation.objects.count()
        supported_orgs = Institution.objects.count()
        foundations = Institution.objects.filter(type__icontains="FD")
        ngos = Institution.objects.filter(type__icontains="NG")
        local_fundraisings = Institution.objects.filter(type__icontains="LF")
        context = {
            "total_bags": total_bags,
            "supported_orgs": supported_orgs,
            "foundations": foundations,
            "ngos": ngos,
            "local_fundraisings": local_fundraisings
        }
        return render(request, "index.html", context)


class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")


class Login(View):
    def get(self, request):
        return render(request, 'login.html')


class Register(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            username = email  # Przyjmowanie emaila jako nazwy użytkownika
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = name
            user.last_name = surname
            user.save()
            return redirect('login')
        return render(request, 'register.html', {'form': form})