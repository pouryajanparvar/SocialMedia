from django.shortcuts import render
from django.views import View
from .forms import UserRegistrationsForm
# Create your views here.


class UserRegisterView(View):
    def get(self, request):
        context = {
            'form' : UserRegistrationsForm()
        }
        return render(request, 'accounts/register_page.html', context)

    def post(self, request):
        pass


