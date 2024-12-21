from django.shortcuts import render, redirect, HttpResponse
from . models import Listing, Location, Agent
from . forms import ListingForm, AgentForm
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

def homepage(request):

  if 'search' in request.GET:
    search = request.GET.get('search')

    listings = Listing.objects.filter(location__icontains=search)

  else:
    listings = Listing.objects.all()

  listings = Listing.objects.all()
  locations = Location.objects.all()

  context = {'listings': listings, 'locations': locations}
  return render(request, 'home.html', context)


@login_required(login_url="login")
def create(request):

  form = ListingForm()
  
  if request.method == "POST":
    form = ListingForm(request.POST, request.FILES)
    if form.is_valid():
      form = form.save(commit=False)
      #form.agent.username = request.user
      Listing.objects.create(agent__name__username=request.user.username)

      form.save()
      return redirect('homepage')
    else:
      messages.info(request, 'Something Went Wrong!')
      return redirect('create')

  context = {'form': form}

  return render(request, 'create.html', context)


@login_required(login_url="login")
def update(request, pk):
  listing = Listing.objects.get(id=pk)
  form = ListingForm(instance=listing)

  if request.user != listing.agent.name:
    return HttpResponse("You cannot Update another Agent's property")

  if request.method == "POST":
    form = ListingForm(request.POST, request.FILES, instance=listing)
    if form.is_valid:
      form.save()
      return redirect('homepage')
    else:
      messages.info(request, 'Something Went Wrong!')
      return redirect('update')

  context = {'form': form}
  return render(request, 'update.html', context)



def read(request, pk):
  
  listing = Listing.objects.get(id=pk)
  agent = Agent.objects.get(name=listing.agent.name.id)

  context = {'listing': listing, 'agent': agent}
  return render(request, 'read.html', context)



@login_required(login_url="login")
def delete(request, pk):
  listing = Listing.objects.get(id=pk)

  if request.user == listing.agent.name:
    listing.delete()
    return redirect('homepage')
  else:
    return HttpResponse('You are not Authorized!')


@login_required(login_url="login")
def account(request):


  form = AgentForm()
  if request.method == "POST":
    form = AgentForm(request.POST, request.FILES)
    if form.is_valid():
      form = form.save(commit=False)
      form.name = request.user
      form.save()
      return redirect('homepage')
    else:
      messages.info(request, 'Something Went Wrong!')
      return redirect('contact')
  context = {'form': form}
  return render(request, 'account.html', context)


@login_required(login_url='login')
def account_update(request, pk):

  agent = Agent.objects.get(id=pk)
  form = AgentForm(instance=agent)

  if request.user != agent.name:
    return HttpResponse('Not your account')

  if request.method == "POST":
    form = AgentForm(request.POST, request.FILES, instance=agent)
    if form.is_valid():
      form.save()
      return redirect('homepage')
    else:
      messages.info(request, 'Something Went Wrong!')
      return redirect('account_update')

  context = {'form': form}
  return render(request, 'account_update.html', context)


def agents(request):
  agents = Agent.objects.all()
  context = {'agents': agents}
  return render(request, 'agents.html', context)


def agent_details(request, pk):
  agent = Agent.objects.get(id=pk)
  listings = Listing.objects.filter(agent=agent)
 
  context = {'agent': agent, 'listings': listings}
  return render(request, 'agent_detail.html', context)

@login_required(login_url="login")
def agent_delete(request, pk):
  #agent = Agent.objects.get(id=pk)
  agent = User.objects.get(username=request.user)

  if request.user == agent:
    agent.delete()
    return redirect('homepage')
  else:
    return HttpResponse("You can't delete another agent")


  
  