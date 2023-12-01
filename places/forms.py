from django import forms
from places.models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widget = {
            'user': forms.Select(attrs={'readonly': 'readonly'}),
        }
