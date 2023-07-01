from django.contrib.auth.models import User
from django.db import models
from phone_field import PhoneField
from django.utils.translation import gettext as _


class Category(models.Model):
    name = models.CharField(max_length=64)


class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    class Type(models.TextChoices):
       FOUNDATION = "FD", _("foundation")
       NGO = "NG", _("non-governmental organization")
       LOCAL_FUNDRAISING = "LF", _("local fundraising")

    type = models.CharField(choices=Type.choices, default=Type.FOUNDATION, max_length=2)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.PositiveSmallIntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField()
    phone_number = PhoneField(blank=True, help_text=_('Contact phone number'))
    city = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=5)
    pick_up_date = models.DateField(auto_now_add=True)
    pick_up_time = models.TimeField(auto_now_add=True)
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    