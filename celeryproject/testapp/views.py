from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect,render

from .forms import GenerateRandomUserForm
from .task import create_random_user_accounts

'''class GenerateRandomUserView(FormView):
    template_name = 'testapp/generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('users_list')'''

def generate_view(request):
	
	create_random_user_accounts.delay('hello')
	return render(request,'testapp/generate_random_users.html')

def popup_view(request):
	
	flag=True
	print("inside popup_view!!!!!!!!!!!!!!!!!!!")
	return render(request,'testapp/generate_random_users.html')
