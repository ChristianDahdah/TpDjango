from django import forms


class RechercheForm(forms.Form):
    query = forms.CharField(max_length=100)
