from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Location(models.Model):
  name = models.CharField(max_length=255)

  class Meta:
    ordering = ['name']

  def __str__(self):
      return self.name
  


class Agent(models.Model):
  name = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='profile_img')
  phone = models.PositiveIntegerField()
  mobile = models.PositiveIntegerField()
  about = models.TextField(max_length=1000)

  def __str__(self):
      return self.name.username
  


class Listing(models.Model):

  ELEVATOR = {'YES': 'Yes', 'NO':'No'}
  STATUS = {'RENT': 'Rent', 'SALE': 'Sale'}
  PROPERTY_TYPE = {'FLAT': 'Flat', 'Apartment': 'Apartment', 'ROOFTOP': 'Rooftop', 'PENTHOUSE': 'Penthouse', 'DUPLEX': 'Duplex'}

  agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
  status = models.CharField(choices=STATUS, max_length=10)
  property_type = models.CharField(choices=PROPERTY_TYPE, max_length=15)
  title = models.CharField(max_length=255)
  image = models.ImageField(upload_to='images')
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  price = models.PositiveIntegerField()
  area = models.PositiveIntegerField()
  beds = models.PositiveIntegerField()
  baths = models.PositiveIntegerField()
  garage = models.PositiveIntegerField()
  elevator = models.CharField(choices=ELEVATOR, max_length=3)
  description = models.TextField(max_length=10000)


  class Meta:
    ordering = ['title']

  def __str__(self):
      return self.title


  

