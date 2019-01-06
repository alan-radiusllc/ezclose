from django import forms
from django.forms import modelform_factory
from django.contrib.auth.models import User
from ezclose.models import UserProfile, Transactions, Tasks, Team, TeamType, TeamMember, Property
from django_select2.forms import Select2MultipleWidget, ModelSelect2Widget
from django.utils.translation import ugettext_lazy as _

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
        labels = {'isRealtor' : _('I am a Realtor'),
                  'phone1'    : _('Primary Phone'), 
                  'phone1Type': _('Primary Phone Type'),
                  'phone2'    : _('Secondary Phone'), 
                  'phone2Type': _('Secondary Phone Type'),}
        def __init__(self, *args, **kwargs):
            super(UserProfileForm, self).__init__(*args, **kwargs)
            self.fields['isRealtor'].label = "I am a Realtor"

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
        
#class AddTeamMemberForm(forms.Form):
#	type = forms.ModelChoiceField(
#	    queryset=TeamType.objects.all(), 
#	    label = u"Type", 
#	    widget=ModelSelect2Widget(
#	         queryset=TeamType.objects.all(),
#	         model=TeamType, 
#	         search_fields=['name__icontains'],
#	    )
#	)
#	     
#	member = forms.ModelChoiceField(
#	    queryset=TeamMember.objects.all(), 
#	    label = u"Member",
#	    widget=ModelSelect2Widget(
#	         model=TeamMember, 
	    #    search_fields=['type__icontains'],
	    #    dependent_fields={'type': 'type'}, 
	    #    max_results=50,
#	    )
#	)
		
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('mls', 'type', 'picture')
    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)
        self.fields['mls'].label = "MLS"

class AddTeamMemberForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('type', 'member')

    def __init__(self, *args, **kwargs):
        super(AddTeamMemberForm, self).__init__(*args, **kwargs)
        self.fields['member'].queryset = TeamMember.objects.none()
        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['member'].queryset = TeamMember.objects.filter(type_id=type_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['member'].queryset = self.instance.type.member_set
		
class TaskForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
       		 super(TaskForm, self).__init__(*args, **kwargs)
        	 self.fields['group'].label = ''
	class Meta:
		model = Tasks
		fields = ('name', 'group', 'dueDate', 'assignee', 'status')
		widgets = {'name':    forms.TextInput(attrs={'disabled': True}),
		           'group':   forms.TextInput(attrs={'disabled': True}),
		           'dueDate': forms.TextInput(attrs={'disabled': True}),
		           'status':  forms.Select(attrs={"onChange":'form.submit()'})
		}
	