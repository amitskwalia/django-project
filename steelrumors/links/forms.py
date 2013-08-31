from django import forms
from .models import UserProfile
from .models import Link

class UserProfileForm(forms.ModelForm):
	class Meta:
		model=UserProfile
	
		
class LinkForm(forms.ModelForm):
	class Meta:
		model=Link
		exclude = ("submitter", "rank_score")
		
