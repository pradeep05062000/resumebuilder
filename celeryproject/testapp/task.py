import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from testapp import views
#from django.http import request
from celery import shared_task

@shared_task
def create_random_user_accounts(request):
	
	print(request)
	return 'succes!!!!!!!!!!'
	








