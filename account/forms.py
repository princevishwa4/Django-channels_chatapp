from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from simplemathcaptcha.fields import MathCaptchaField
from simplemathcaptcha.widgets import MathCaptchaWidget


class RegisterForm(UserCreationForm):
	password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
	password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']
		labels = {'first_name' : 'First Name', 'last_name' : 'Last Name', 'email' : 'Email'}
		widgets = {'username' : forms.TextInput(attrs={'class' : 'form-control'}), 
					'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
					'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
					'email' : forms.EmailInput(attrs={'class' : 'form-control'})}


class LoginForm(AuthenticationForm, MathCaptchaField):
	username = UsernameField(widget=forms.TextInput(attrs={'autofocus' : True, 'class' : 'form-control'}))
	password = forms.CharField(strip=False, widget=forms.PasswordInput(attrs={'autocomplete' : 'current-password', 'class' : 'form-control'}))
	captcha = MathCaptchaField(widget=MathCaptchaWidget(question_tmpl="What is the result of %(num1)i %(operator)s %(num2)i?"))


class UpdateForm(forms.ModelForm):
	# username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	# first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	# last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	# email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    	
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']
		labels = {'first_name' : 'First Name', 'last_name' : 'Last Name', 'email' : 'Email'}
		widgets = {'username' : forms.TextInput(attrs={'class' : 'form-control'}), 
					'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
					'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
					'email' : forms.EmailInput(attrs={'class' : 'form-control'})}

	def clean_username(self):
		username = self.cleaned_data.get('username')
		print(self.instance.id)
		try:
			account = User.objects.exclude(id=self.instance.id).get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Username is already been used by another user.')		

	def clean_email(self):
		email = self.cleaned_data.get('email')
		try:
			account = User.objects.exclude(id=self.instance.id).get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email is already been used by another user.')

	def save(self, commit=True):
		user = super(UpdateForm, self).save(commit=False)
		user.username = self.cleaned_data['username']
		user.email = self.cleaned_data['email'].lower()

		if commit:
			user.save()
		return user