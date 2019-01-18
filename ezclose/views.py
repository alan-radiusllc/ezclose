# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from ezclose.models import DefaultMilestones, Tasks, Transactions, DefaultTasks, Team, Realtor, Client, TeamMember, Property, UserProfile
from ezclose.forms import UserForm, UserProfileForm, TransactionForm, TaskForm, AddTeamMemberForm, PropertyForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.template.defaultfilters import slugify
from django.forms import formset_factory, modelformset_factory
from django.shortcuts import redirect

import datetime

#from ezclose.forms import DefaultMilestonesForm

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
        
@csrf_protect
@login_required
def overview(request):
    #return HttpResponse("Hello from EZ-Close. <a href='/ezclose/about/'> About</a>")
    milestone_list = DefaultMilestones.objects.order_by('name')[:5]
    transaction_list = Transactions.objects.filter(client__user=request.user).order_by('client')[:15]
    context_dict = {'milestones': milestone_list, 'transactions': transaction_list}
    #context_dict = {'boldmessage': "crunchy!"}
    return render(request, 'ezclose/overview.html', context=context_dict)

@csrf_protect
@login_required
def realtor_overview(request):
    #return HttpResponse("Hello from EZ-Close. <a href='/ezclose/about/'> About</a>")
    milestone_list = DefaultMilestones.objects.order_by('name')[:5]
    transaction_list = Transactions.objects.filter(realtor__user=request.user).order_by('client')[:15]
    context_dict = {'milestones': milestone_list, 'transactions': transaction_list}
    #context_dict = {'boldmessage': "crunchy!"}
    return render(request, 'ezclose/overview.html', context=context_dict)

@csrf_protect
@login_required
def most_recent(request):
    mr_trans = Transactions.objects.filter(client__user=request.user).order_by('-startDate')[0]
    context_dict = {}
    return(show_transactions(request, mr_trans.slug))
    #try:
    #    #transact = Transactions.objects.get(slug=transaction_name_slug)
    #    tasks    = Tasks.objects.filter(transaction=mr_trans)
    #    context_dict['transaction'] = mr_trans
    #    context_dict['tasks'] = tasks

    #except Transaction.DoesNotExist:
    #    context_dict['tasks'] = None
    #    context_dict['transaction'] = None
    
    #return render(request, 'ezclose/transaction.html', context_dict)
    
def index(request):
    milestone_list = DefaultMilestones.objects.order_by('name')[:5]
    transaction_list = Transactions.objects.order_by('startDate')[:15]
    context_dict = {'milestones': milestone_list, 'transactions': transaction_list}
    #context_dict = {'boldmessage': "crunchy!"}
    return render(request, 'ezclose/index.html', context=context_dict)
    
def about(request):
    #return HttpResponse("This is the about! <a href='/ezclose/'> Index</a>")
    if request.user.is_authenticated():
        up = request.user.userprofile.isRealtor
    else:
        up = False
    
    context_dict = {'italicmessage': "crispy!", 'is_a_realtor' : up }
    return render(request, 'ezclose/about.html', context=context_dict)

def client_list(request):
    #return HttpResponse("This is the about! <a href='/ezclose/'> Index</a>")
    if request.user.is_authenticated():
        up = request.user.userprofile.isRealtor
    else:
        up = False
    
    context_dict = {'italicmessage': "crispy!", 'is_a_realtor' : up }
    return render(request, 'ezclose/about.html', context=context_dict)

def account(request):
	context_dict = {'italicmessage': "account info"}
	return render(request, 'ezclose/about.html', context=context_dict)
	# Note: update to give account information - name, address, email, phone, 
	
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

    TaskFormSet = modelformset_factory(Tasks, fields = ('name', 'group', 'dueDate', 'status',), extra=0)
    if request.method == 'POST':
        formset = TaskFormSet(data=request.POST)
        print("post form")
        if formset.is_valid():
            formset.save()
    else:
        formset = TaskFormSet(queryset = tasks)
        print("populate form")

    taskForm = zip(tasks, formset)
    #print (taskForm)
    #for form in formset:
    #	print(form.as_table())    
    return render(request, 'ezclose/task_detail.html', {'formset': formset, 'tasks': tasks, 'transaction': transact, 'taskform': taskForm })
 
def show_team(request, transaction_name_slug):
    context_dict = {}
    try:
        transact = Transactions.objects.get(slug=transaction_name_slug)
        team    = Team.objects.filter(transaction=transact)
        context_dict['transaction'] = transact
        context_dict['team'] = team

    except Transactions.DoesNotExist:
        context_dict['team'] = None
        context_dict['transaction'] = None
    
    return render(request, 'ezclose/team.html', context_dict)
    
def addRealtorToTeam(transaction, realtor):
	return

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
            profile.save()
            
            if profile.isRealtor:
                realtor = Realtor.objects.get_or_create(user=profile.user,name=profile.name,
                    phone1=profile.phone1,email=user.email)[0]
                realtor.phone2 = profile.phone2
                realtor.phone1Type = profile.phone1Type
                realtor.phone2Type = profile.phone2Type
                realtor.brokerage = profile.brokerage
                realtor.save()
            # if 'picture' in request.FILES:
            #     profile.picture = request.FILES['picture']
            else:
                client = Client.objects.get_or_create(user=profile.user,name=profile.name,
                    phone1=profile.phone1,email=user.email,newCustomer=True)[0]
                client.phone2 = profile.phone2
                client.phone1Type = profile.phone1Type
                client.phone2Type = profile.phone2Type
                client.street = profile.street
                
                client.save()
            registered = True
            username = request.POST.get('username')
            password = request.POST.get('password')
            userlogin = authenticate(username=username, password=password)
            login(request, userlogin)
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

@csrf_protect
def user_login(request):
    if request.method == 'POST':
        # Gather from login form
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                numClient = Client.objects.filter(user=user).count()
                if numClient > 0:
                    theClient = Client.objects.filter(user=user).get()
                    numTran = Transactions.objects.filter(client=theClient).count()
                    if numTran > 0:
                        return HttpResponseRedirect(reverse('most_recent'))
                    else:
                        return HttpResponseRedirect(reverse('overview'))
                else:
                    return HttpResponseRedirect(reverse('overview'))
            else:
                return HttpResponse("Your account is disabled")
        else:
            print("Invalid login: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login")
    else:
        return render(request, 'ezclose/login.html', {})

def new_transaction(request):
    created_new_transaction = False
    if request.user.is_authenticated():
        up = request.user.userprofile.isRealtor
    else:
        up = False
    if request.method == 'POST':
        newT_form = TransactionForm(data = request.POST)
        if newT_form.is_valid():
            print ("valid form")
            newT = newT_form.save(commit=False)
            # add in the required stuff
            newT.status="ACTIVE"
            newT.active = True
            newT.startDate = datetime.datetime.now()
            newT.slug = datetime.datetime.now()
            newT.save()
            # For slug, use client name and Transaction ID
            
            # Copy in default Tasks
            # query default tasks for transaction type
            # query for the tags we have, and locality
            # insert those into the Tasks table with this transaction id
            print(newT.transactionType)
            if newT.transactionType == 'BUY' or newT.transactionType == 'SELL':
                tasks = DefaultTasks.objects.filter(purchase=newT.transactionType)
            else:
                tasks = DefaultTasks.objects.all()
            for t in tasks:
                ntTransaction = newT
                ntName = t.name
                ntGroup = t.group
                ntCategory = t.category
                ntWbs = t.wbs
                ntPre = t.prerequisites
                ntStatus = 'READY'
                if t.assignee == 'AGENT':
                    ntAssign = newT.realtor.user
                else:
                    if t.assignee == 'CLIENT':
                        ntAssign = newT.client.user
                    else: 
                        ntAssign = newT.client.user   # need way to have multiple assignees, or "team"
                ntOver = False
                ntSlug = slugify(ntName + str(newT.id))

                addTask = Tasks.objects.get_or_create(transaction=newT, name=ntName, group = ntGroup,
                           category=ntCategory, wbs=ntWbs, prerequisites=ntPre, status=ntStatus,
                           assignee=ntAssign, overDue=ntOver,slug=ntSlug)[0]
                addTask.save()
                # add the realtor to the team?
            created_new_transaction = True
            if up:
                return redirect('/ezclose/realtor_overview/')
            else:
                return redirect('/ezclose/overview/')
        else:
            print("errors!")
            print(newT_form.errors)
    else: 
        # Not a POST
        print ("not a POST")

        if (up):
            theRealtor = Realtor.objects.filter(user=request.user).get()
            newT_form = TransactionForm(initial={'realtor': theRealtor})
        else:
            theClient = Client.objects.filter(user=request.user).get()
            newT_form = TransactionForm(initial={'client': theClient })
    
    return render(request, 'ezclose/new_transaction.html',
                  {'newT_form': newT_form,
                   'created_new_transaction': created_new_transaction})

def set_property(request, transaction_name_slug):
    property_set = False
    if request.method == 'POST':
        prop_form = PropertyForm(data = request.POST)
        if prop_form.is_valid():
            prop = prop_form.save(commit=False)
            
            # add in the required stuff
            transact = Transactions.objects.get(slug=transaction_name_slug)
            
            # look up address and so forth from web if possible
            prop.save()
            transact.property = prop
            transact.save()
            property_set = True
            return redirect('/ezclose/transaction/'+transaction_name_slug)
        else:
            print(prop_form.errors)
    else: 
        # Not a POST
        transact = Transactions.objects.get(slug=transaction_name_slug)
        if transact.property:
            print (transact.property.type)
            prop_form = PropertyForm(initial={'mls': transact.property, 'type': transact.property.type, 'picture': transact.property.picture })
        else:
            prop_form = PropertyForm()
    
    trns = Transactions.objects.get(slug=transaction_name_slug)
    return render(request, 'ezclose/set_property.html',
                  {'prop_form': prop_form,
                   'set_property': set_property,
                   'trns': trns})
                    
def add_team_member(request, transaction_name_slug):
    added_new_member = False
    if request.method == 'POST':
        newTM_form = AddTeamMemberForm(data = request.POST)
        if newTM_form.is_valid():
            newTM = newTM_form.save(commit=False)
            
            # add in the required stuff
            transact = Transactions.objects.get(slug=transaction_name_slug)
            newTM.transaction = transact
            newTM.dateAdded = datetime.datetime.now()
            newTM.dateChanged = datetime.datetime.now()
            newTM.save()
            
            added_new_member = True
            return redirect('/ezclose/team/'+transaction_name_slug)
        else:
            print(newTM_form.errors)
    else: 
        # Not a POST
        newTM_form = AddTeamMemberForm()
    
    trns = Transactions.objects.get(slug=transaction_name_slug)
    return render(request, 'ezclose/new_team_member.html',
                  {'newTM_form': newTM_form,
                   'added_new_member': added_new_member,
                   'trns': trns})
                    
def load_teamMembers(request):
    type_id = request.GET.get('type')
    members = TeamMember.objects.filter(type_id=type_id)
    return render(request, 'ezclose/member_dropdown_list.html', {'members': members})
    

#def client_confirm(request):
#    if request.method == 'POST':
#        # Gather from confirm form
#        realtor_name = request.POST.get('realtorName')
#        #password = request.POST.get('password')
#        realtor = Realtor.objects.get(name = realtor_name)
#        if realtor:
#            if realtor.is_active:
#                login(request, user)
#                return HttpResponseRedirect(reverse('most_recent'))
#            else:
#                return HttpResponse("Your account is disabled")
#        else:
#            print("Invalid login: {0}, {1}".format(username, password))
#            return HttpResponse("Invalid login")
#    else:
#        return render(request, 'ezclose/login.html', {})
            
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