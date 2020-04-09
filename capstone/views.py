from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .load_csv_data import load_csv_data
from .allocation import allocate,swap
from django.contrib.auth.decorators import login_required
from .models import Booth, Map
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json

from django.http import JsonResponse, HttpResponse

# Create your views here.
@login_required
def home(request):

	print(request.user)
	user = request.user
	user_maps = Map.objects.filter(user=request.user)    
	curr_map = user_maps[0]
	print(user_maps[0].booths.all())
	booth = curr_map.booths.all()
	if request.method == 'POST':
		allocate(booth)
	json_serializer = serializers.get_serializer("json")()
	booths = json_serializer.serialize(booth , ensure_ascii = False)
	json_serializer = serializers.get_serializer("json")()
	maps = json_serializer.serialize(user_maps, ensure_ascii = False)


	return render(request,'capstone/home.html',{'booth':booths})

	# return render(request,'capstone/home.html',{'maps':maps},{'booth':booths})

@login_required
def csv(request):
	print("this iss called")
	if request.method == 'POST' and request.FILES['input']:
		myfile = request.FILES['input']
		fs = FileSystemStorage()
		filename = fs.save("data.xlsx", myfile)
		load_csv_data(filename,request)
		return redirect('/')
	return render(request, 'capstone/csv.html')

def create_account(request):
	if request.method == 'POST':
		# Create user and save to the database
		user = User.objects.create_user(request.POST['username'], '', request.POST['password'])
		map = Map()
		map.user = user
		map.name = "current_map"
		map.save()
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

# @csrf_exempt 
# 	# return render(request,'accounts/change_allocation')

# @api_view(['POST'])
@csrf_exempt
def change_allocation(request):
	if request.method == "POST":
		print("change allocation data posted")
		output = json.loads(request.body) 
		user_maps = Map.objects.filter(user=request.user)    
		curr_map = user_maps[0]
		edit_map = Map.objects.get(pk=curr_map.curr_map_ref)
		booths = edit_map.booths
		for booth in booths.all():
   		     booth.delete()
		for project in output:
			booth = Booth()
			booth.project_id = project.get('project_id')
			booth.length = project.get('length')
			booth.width = project.get('width')
			booth.area = project.get('area')
			booth.project_name = project.get('project_name')
			booth.industry = project.get('industry')
			booth.length_pixel = project.get('length_pixel')
			booth.width_pixel = project.get('width_pixel')
			booth.rotation = project.get('rotation')
			booth.position_x = project.get('position_x')
			booth.position_y = project.get('position_y')
			booth.in_campus_centre = project.get('in_campus_centre')
			booth.saved_map = edit_map
			booth.save()





	return JsonResponse({"success":True})