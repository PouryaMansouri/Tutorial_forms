from django import forms


class CustomerForm(forms.Form):
    name = forms.CharField(max_length=150, label='Full name')
    email = forms.EmailField(help_text='customer email')
    birthday = forms.DateField(required=False, error_messages={'invalid': 'Error, example 10/10/2020 '})
    phone = forms.CharField(max_length=13, required=False)
    address = forms.CharField(widget=forms.Textarea)
    status = forms.IntegerField(required=False)
