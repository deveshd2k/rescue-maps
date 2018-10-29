from django import forms
from django.forms import ModelForm
from .models import userData,Profile,userInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
	orgName = forms.CharField(max_length=30)
	rescueHome = forms.CharField(max_length=30)
	bedsno = forms.CharField(max_length=4)
	contact = forms.CharField(max_length=13)

class Meta:
	model = User
	fields = ('username', 'orgName', 'rescueHome','bedsno', 'contact', 'password1', 'password2' )

	def clean_username(self):
		username = self.cleaned_data['username'].lower()
		r = User.objects.filter(username=username)
		if r.count():
			raise  ValidationError("Username already exists")
		return username

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise ValidationError("Passwords don't match")
			return password2

class userForm(ModelForm):

	class Meta:
		model = userData
		fields = ('rescueHome','amenities','waterlevel','levelchange','feedback','degree')

class userInfoform(ModelForm):

	class Meta:
		model = userInfo
		fields = ('username','name','email','contact','family')