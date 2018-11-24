from django import forms
from django.contrib.auth.models import User
from ezclose.models import UserProfile, Transactions, Tasks

#class DefaultMilestonesForm(forms.ModelForm):
#    name = forms.CharField(max_length=128, help_text="Enter the milestone name")
#    type = forms.CharField(max_length=128, help_text="Enter the type")
#    
#    class Meta:
#        model = DefaultMilestones

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'phone1', 'phone1Type', 'phone2', 'phone2Type', 'street', 'street2',
                   'city', 'zipcode', 'picture', 'isRealtor', 'brokerage')

'''
class Transactions(models.Model):
	realtor         = models.ForeignKey(Realtor)
	client          = models.ForeignKey(Client)
	transactionType = models.CharField(max_length=20, choices=TRANSACTION_TYPES) 
	property        = models.ForeignKey(Property, blank=True, null=True) 
	status          = models.CharField(max_length=10, choices=TRANSACTION_STATUS)
	active          = models.BooleanField() # redundant?
	startDate       = models.DateTimeField()
	endDate         = models.DateTimeField(blank=True, null=True)
	lastActivity    = models.DateTimeField(blank=True, null=True)
	# team          = models.ForeignKey(Team)  # add when Team class is ready
	slug            = models.SlugField(unique=True)
	# tags? Use these here to indicate which ones we need from the Default tasks?
	tag1            = models.CharField(max_length=12, choices=TAGS, blank=True, null=True)
	tag2            = models.CharField(max_length=12, choices=TAGS, blank=True, null=True)
	tag3            = models.CharField(max_length=12, cho
	'''
	
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ('realtor', 'client', 'transactionType', 'tag1', 'tag2', 'tag3')
        

		