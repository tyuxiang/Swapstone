from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .load_csv_data import load_csv_data
from .allocation import allocate
from django.contrib.auth.decorators import login_required
from .models import Booth, Map
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages


# Create your views here.
@login_required
def home(request,map=None):
	if not map:
		user = request.user
		maps = Map.objects.filter(user=user)
		x = len(maps)-1
		booth = Booth.objects.filter(saved_map = maps[x])
	else:
		booth = Booth.objects.filter(saved_map = map)
	json_serializer = serializers.get_serializer("json")()
	booths = json_serializer.serialize(booth , ensure_ascii = False)
	# return render(request,'capstone/home.html',{'maps':maps},{'booth':booths})
	return render(request,'capstone/home.html',{'booth':booths})
	#return render(request,'capstone/home.html')

@login_required
def csv(request):
	if request.method == 'POST' and request.FILES['input']:
		myfile = request.FILES['input']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url =filename
		map = load_csv_data(uploaded_file_url,request)
		booths = Booth.objects.filter(saved_map = map)
		allocate(booths)
		# return home(request,map)
	return render(request, 'capstone/csv.html')

def create_account(request):
	if request.method == 'POST':
		# Create user and save to the database
		user = User.objects.create_user(request.POST['username'], '', request.POST['password'])

		# Update fields and then save again
		# user.first_name = 'John'
		# user.last_name = 'Citizen'
		# user.save()
	return render(request,'registration/create_account.html')

@login_required
def change_password(request):
	form = PasswordChangeForm(request.user)
	if request.method == 'POST':
		form = PasswordChangeForm(user=request.user, data=request.POST)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, 'Your password was successfully updated!')
		else:
			messages.error(request, 'Please correct the error above')
	return render(request,'registration/change_password.html',{'form':form})

def reset_password(request):
	if request.method == 'POST':
		# Reset Password
		print("not done yet")
	return render(request,'registration/reset_password.html')

