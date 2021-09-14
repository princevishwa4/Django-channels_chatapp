from django import forms

from chat.models import Room


class RoomForm(forms.ModelForm):
	name = forms.ModelChoiceField(queryset=Room.objects.all(), widget=forms.Select(attrs={'class' : 'form-control'}))
	class Meta:
		model = Room
		fields = ['name']
		labels = {'name' : 'Room Name'}	