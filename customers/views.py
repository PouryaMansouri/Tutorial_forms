from django.shortcuts import render
# Create your views here.
from django.views import View

from . import forms


class CreateCustomer(View):

    def post(self, request):
        form = forms.CustomerForm(self.request.POST)
        if form.is_valid():
            pass
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
