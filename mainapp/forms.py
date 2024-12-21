from django.forms import ModelForm
from . models import Listing, Agent


class ListingForm(ModelForm):
  class Meta:
    model = Listing
    fields = [
      #'agent',
      'status',
      'property_type',
      'title',
      'image',
      'location',
      'price',
      'area',
      'beds',
      'baths',
      'garage',
      'elevator',
      'description',
    ]

class AgentForm(ModelForm):
  class Meta:
    model = Agent
    fields = [
      'image',
      'phone',
      'mobile',
      'about',
    ]