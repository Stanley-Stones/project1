from django.urls import path
from . import views as mainviews


urlpatterns = [
  path('', mainviews.homepage, name = 'homepage'),
  path('create/', mainviews.create, name = 'create'),
  path('update/<str:pk>/', mainviews.update, name = 'update'),
  path('property/<str:pk>/', mainviews.read, name = 'read'),
  path('delete/<str:pk>/', mainviews.delete, name = 'delete'),

  path('account/', mainviews.account, name = 'account'),
  path('account_update/<str:pk>/', mainviews.account_update, name = 'account_update'),

  path('agents/', mainviews.agents, name = 'agents'),
  path('agent/<str:pk>/', mainviews.agent_details, name = 'agent_details'),
  path('agent_delete/<str:pk>/', mainviews.agent_delete, name = 'agent_delete'),
]