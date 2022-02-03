from django.shortcuts import render, HttpResponse
# Create your views here.
from django.views import View

from . import forms
from .models import Customer


class CreateCustomer(View):

    def post(self, request):
        form = forms.CustomerForm(self.request.POST)
        form = forms.CustomerForm()
        if form.is_valid():
            name = form.cleaned_data['name']
            birthday = form.cleaned_data['birthday']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            status = form.cleaned_data['status']
            phone = form.cleaned_data['phone']
            c1 = Customer.objects.create(name=name, birthday=birthday, phone=phone, email=email,
                                         address=address)
            return HttpResponse('Thanks,Customer create')

        context = {
            'create_form': form
        }
        return render(request=self.request, template_name='customers/create_form.html', context=context)

    def get(self, request):
        form = forms.CustomerForm()
        context = {
            'create_form': form
        }
        return render(request=self.request, template_name='customers/create_form.html', context=context)
