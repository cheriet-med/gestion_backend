from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from googletrans import Translator
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])




class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, is_superuser=True,**extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, is_superuser=True, **extra_fields)

        user.set_password(password)
        user.save()

        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(max_length=1000,blank=True, null=True)
    last_name = models.CharField(max_length=1000,blank=True, null=True)
    adress = models.CharField(max_length=1000,blank=True, null=True)
    city = models.CharField(max_length=1000,blank=True, null=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email
    



class Personel(models.Model):
    prenom = models.CharField(max_length=10000,blank=True, null=True)
    nom = models.CharField(max_length=10000,blank=True, null=True)
    sex = models.CharField(max_length=10000,blank=True, null=True)
    adress = models.CharField(max_length=10000,blank=True, null=True)
    naissance = models.DateField(max_length=10000,blank=True, null=True)
    entre = models.DateField(max_length=10000,blank=True, null=True)
    enfant = models.IntegerField(max_length=10000,blank=True, null=True)
    prenom_femme = models.CharField(max_length=10000,blank=True, null=True)
    prenom_pere = models.CharField(max_length=10000,blank=True, null=True)
    nom_mere = models.CharField(max_length=10000,blank=True, null=True)
    prenom_mere = models.CharField(max_length=10000,blank=True, null=True)
    tel = models.IntegerField(max_length=10000,blank=True, null=True)



class Avancement(models.Model):
    nombre_de_degree = models.IntegerField(max_length=10000,blank=True, null=True)
    nombre_de_echlon = models.IntegerField(max_length=10000,blank=True, null=True)
    date_avencement = models.DateField(max_length=10000,blank=True, null=True)
    id_avencement_personel = models.IntegerField(max_length=10000,blank=True, null=True)



class Absance(models.Model):
    type_abssence = models.CharField(max_length=10000,blank=True, null=True)
    decision_abssence = models.CharField(max_length=10000,blank=True, null=True)


class Sanction(models.Model):
    date_sanction = models.DateField(max_length=10000,blank=True, null=True)
    duree_sanction = models.IntegerField(max_length=10000,blank=True, null=True)
    type_sanction = models.CharField(max_length=10000,blank=True, null=True)


class Randement(models.Model):
    degree_rendement = models.IntegerField(max_length=10000,blank=True, null=True)
    
    
class Conge(models.Model):
    date_debut = models.DateField(max_length=10000,blank=True, null=True)
    duree_fin = models.DateField(max_length=10000,blank=True, null=True)
    type_conge = models.CharField(max_length=10000,blank=True, null=True)