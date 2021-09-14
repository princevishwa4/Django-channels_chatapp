from django import forms
from django.utils.safestring import mark_safe

from chat.models import Room


class RoomForm(forms.ModelForm):
	name = forms.ModelChoiceField(queryset=Room.objects.all(), widget=forms.Select(attrs={'class' : 'form-control'}), label=mark_safe("<strong>Select Room Name</strong>"))
	class Meta:
		model = Room
		fields = ['name']