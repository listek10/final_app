from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Product
from django.views.generic import CreateView


def home(request, *args, **kwargs):
    return render(request, "index.html", {});


def loginPage(request, *args, **kwargs):
    return HttpResponse(request, "loginPage.html");


def loggedUser(request, *args, **kwargs):
    return HttpResponse(request, "loggedUser.html", {});


def showOffer(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "offer.html", context);


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'registration/login.html'

    def form_valid(self, form):
        response = super(SignUpView, self).form_valid(form)
        user = self.object
        login(self.request, self.object)
        return response
