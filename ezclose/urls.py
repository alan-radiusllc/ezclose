"""ez1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from ezclose import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^transaction/(?P<transaction_name_slug>[\w-]+)/$',views.show_transactions, name='show_transactions'),
    url(r'^team/(?P<transaction_name_slug>[\w-]+)/$',views.show_team, name='show_team'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.user_login,name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^overview/$', views.overview, name='overview'),
    url(r'^most_recent/$', views.most_recent, name='most_recent'),
    url(r'^new_transaction/$', views.new_transaction, name='new_transaction'),
    url(r'^add_team_member/(?P<transaction_name_slug>[\w-]+)/$',views.add_team_member, name='add_team_member'),
    url(r'^(?P<pk>\d+)', views.add_team_member, name='update'),
    url(r'ajax/load-members/$', views.load_teamMembers, name='ajax_load_members')
    #url(r'^client_confirm/$', views.client_confirm, name='client_confirm'),
    #url(r'^add_defaultMilestone/$', views.add_defaultMilestone, name='add_defaultMilestone'),
    #url(r'^defaultMilestone/(?P<default_milestone_name_slug>[\w\-]+)/$', views.show_)
    ] 
      
