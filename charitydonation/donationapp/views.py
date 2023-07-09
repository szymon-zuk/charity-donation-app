from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import RegistrationForm, LoginForm, DonationForm
from .models import Donation, Institution, Category


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
            "local_fundraisings": local_fundraisings,
        }
        return render(request, "index.html", context)


class AddDonation(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")
    redirect_field_name = "next"

    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        form = DonationForm()
        return render(request, 'form.html',
                      {'categories': categories, 'institutions': institutions, 'form': form})

    def post(self, request):
        form = DonationForm(request.POST)
        categories = request.POST['categories']
        institution = request.POST['institution']
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            zip_code = form.cleaned_data['zip_code']
            phone_number = form.cleaned_data['phone_number']
            pick_up_date = form.cleaned_data['pick_up_date']
            pick_up_time = form.cleaned_data['pick_up_time']
            pick_up_comment = form.cleaned_data['pick_up_comment']
            user = request.user.id
            donation = Donation.objects.create(quantity=quantity, institution_id=institution, address=address,
                                               city=city, zip_code=zip_code, phone_number=phone_number,
                                               pick_up_date=pick_up_date, pick_up_time=pick_up_time,
                                               pick_up_comment=pick_up_comment, user_id=user)
            donation.categories.add(categories)
            return render(request, 'form-confirmation.html')
        else:
            categories = Category.objects.all()
            institutions = Institution.objects.all()
            return render(request, 'form.html',
                          {'categories': categories, 'institutions': institutions, 'form': form})


class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("landing-page")
            else:
                return redirect("register")
        return render(request, "login.html", {"form": form})


class Register(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            name = form.cleaned_data["name"]
            surname = form.cleaned_data["surname"]
            username = email  # Przyjmowanie emaila jako nazwy użytkownika
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
            user.first_name = name
            user.last_name = surname
            user.save()
            return redirect("login")
        return render(request, "register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("landing-page")
