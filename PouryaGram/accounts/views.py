from django.shortcuts import render
from django.views import View
# Create your views here.


class UserRegisterView(View):
    def get(self, request):
        return render(request, 'accounts/register_page.html')

    def post(self, request):
        pass


