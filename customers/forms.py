from django import forms
from django.utils.translation import ugettext_lazy as _
from customers.models import Customer, Car
from customers.validators import check_phone


#
# class CustomerForm(forms.Form):
#     name = forms.CharField(max_length=150, label='Full name')
#     email = forms.EmailField(help_text='customer email')
#     birthday = forms.DateField(required=False, error_messages={'invalid': 'Error, example 10/10/2020 '},
#                                widget=forms.SelectDateWidget)
#     phone = forms.CharField(max_length=13, required=False)
#     address = forms.CharField(widget=forms.Textarea)
#     status = forms.IntegerField(required=False)
#     image = forms.ImageField()
#     file = forms.FileField()


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        # fields = '__all__'
        exclude = ['status', ]
        labels = {
            'name': _('Full Name'),
            'birthday': _('Birthday')
        }

        widgets = {
            'email': forms.EmailInput(attrs={'name': 'c_email', 'class': 'email form-control', 'id': 'email_id'}, ),
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'phone': forms.TextInput(attrs={'placeholder': 'example 09132985527'})

        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        return check_phone(phone)

    def clean_name(self):
        name: str = self.cleaned_data.get('name')
        return name.capitalize()


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

        widgets = {
            'customer': forms.Select(attrs={'class': 'select2'})
        }
