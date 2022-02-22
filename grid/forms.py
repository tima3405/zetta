from django import forms
from .models import Visits


class DateForm(forms.Form):
    date = forms.DateField()


class AddVisitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddVisitForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

    # sightseeing = forms.Select(attrs={'class': 'form-control', 'placeholder': 'Выберите Тур'},
    # choices=BookNow.sightseeing)

    class Meta:
        model = Visits
        fields = ('__all__')
