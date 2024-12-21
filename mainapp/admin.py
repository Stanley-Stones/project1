from django.contrib import admin
from . models import Listing, Location, Agent

# Register your models here.

admin.site.register(Listing)
admin.site.register(Location)
admin.site.register(Agent)
