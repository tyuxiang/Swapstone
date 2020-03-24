from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .load_csv_data import load_csv_data
from .allocation import allocate
from django.contrib.auth.decorators import login_required
from .models import Booth, Map
from django.core import serializers
from django.contrib.auth.models import User


# Create your views here.
@login_required
def home(request):
	
	user = request.user
	maps = Map.objects.filter(user=user)
	booth = Booth.objects.filter(saved_map = maps.get(id=5))
	json_serializer = serializers.get_serializer("json")()
	booths = json_serializer.serialize(booth , ensure_ascii = False)
	# booths = Booth.objects.all()
	#return render(request,'capstone/home.html',{'maps':maps},{'booth':booths})
	return render(request,'capstone/home.html',{'booth':booths})

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
		return render(request, 'capstone/csv.html')
	return render(request, 'capstone/csv.html')

def create_account(request):
	if request.method == 'POST':
		# Create user and save to the database
		user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

		# Update fields and then save again
		user.first_name = 'John'
		user.last_name = 'Citizen'
		user.save()
	return render(request,'registration/create_account.html')

@login_required
def change_password(request):
	if request.method == 'POST':
		# Change password
		print("not done yet")
	return render(request,'registration/change_password.html')

def reset_password(request):
	if request.method == 'POST':
		# Reset Password
		print("not done yet")
	return render(request,'registration/reset_password.html')

