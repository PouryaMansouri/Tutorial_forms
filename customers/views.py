from django.shortcuts import render, HttpResponse
# Create your views here.
from django.views import View

from . import forms
from .models import Customer


class CreateCustomer(View):

    def post(self, request):
        form = forms.CustomerForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            obj: Customer = form.save(commit=False)
            obj.status = False
            obj.save()
            return HttpResponse('Customer create')
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


class UpdateCustomer(View):

    def get(self, request, pk):
        c = Customer.objects.get(pk=pk)
        form = forms.CustomerForm(instance=c)
        context = {
            'create_form': form
        }
        return render(request=self.request, template_name='customers/create_form.html', context=context)


class CreateCar(View):

    def get(self, request):
        context = {
            'form': forms.CarForm()
        }

        return render(request=self.request, template_name='customers/car_form.html', context=context)
