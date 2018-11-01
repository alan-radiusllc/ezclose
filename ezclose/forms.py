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
        fields = ('website', 'picture')

