from django.shortcuts import render
from django.views import View
from .models import Donation, Institution


class LandingPage(View):
    def get(self, request):
        total_bags = Donation.objects.count()
        supported_orgs = Institution.objects.count()
        context = {
            "total_bags": total_bags,
            "supported_orgs": supported_orgs
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
        return render(request, 'register.html')