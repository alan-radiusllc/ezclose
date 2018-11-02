# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from ezclose.models import DefaultMilestones, Tasks, Transactions
from ezclose.forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required

#from ezclose.forms import DefaultMilestonesForm

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
        
def index(request):
    #return HttpResponse("Hello from EZ-Close. <a href='/ezclose/about/'> About</a>")
    milestone_list = DefaultMilestones.objects.order_by('name')[:5]
    transaction_list = Transactions.objects.order_by('client')[:5]
    context_dict = {'milestones': milestone_list, 'transactions': transaction_list}
    #context_dict = {'boldmessage': "crunchy!"}
    return render(request, 'ezclose/index.html', context=context_dict)
    
def about(request):
    #return HttpResponse("This is the about! <a href='/ezclose/'> Index</a>")
    context_dict = {'italicmessage': "crispy!"}
    return render(request, 'ezclose/about.html', context=context_dict)

def show_transactions(request, transaction_name_slug):
    context_dict = {}
    try:
        transact = Transactions.objects.get(slug=transaction_name_slug)
        tasks    = Tasks.objects.filter(transaction=transact)
        context_dict['transaction'] = transact
        context_dict['tasks'] = tasks

    except Transaction.DoesNotExist:
        context_dict['tasks'] = None
        context_dict['transaction'] = None
    
    return render(request, 'ezclose/transaction.html', context_dict)

def register(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            # if 'picture' in request.FILES:
            #     profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            # errors on form
            print(user_form.errors, profile_form.errors)
    else:
        # not a POST, so adopt the models
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    return render(request, 'ezclose/register.html', 
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})

def user_login(request):
    if request.method == 'POST':
        # Gather from login form
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is disabled")
        else:
            print("Invalid login: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login")
    else:
        return render(request, 'ezclose/login.html', {})
            
                                       
#def add_defaultMilestone(request):
#	form = DefaultMilestonesForm()
#	
#	if request.method == 'POST':
#	    if form.is_valid():
#	        form.save(commit=True)
#	        return index(request)
#	    else:
#	        print(form.errors)
#	
#	return render(request, 'ezclose/add_defaultMilestone.html', {'form': form}