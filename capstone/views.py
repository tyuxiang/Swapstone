from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .load_csv_data import load_csv_data
from .allocation import allocate
from django.contrib.auth.decorators import login_required
from .models import Booth
from django.core import serializers


# Create your views here.
@login_required
def home(request):
	json_serializer = serializers.get_serializer("json")()
	booths = json_serializer.serialize(Booth.objects.all() , ensure_ascii = False)
	# booths = Booth.objects.all()
	return render(request,'capstone/home.html',{'booth':booths})
def login(request):
	return render(request, 'capstone/login_page.html')
def logout(request):
	return render(request, 'capstone/logout.html')

def csv(request):
	if request.method == 'POST' and request.FILES['input']:
		myfile = request.FILES['input']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url =filename
		load_csv_data(uploaded_file_url,request)
		allocate()
		return render(request, 'capstone/csv.html')
	return render(request, 'capstone/csv.html')
	#return render(request, 'capstone/csv.html')

