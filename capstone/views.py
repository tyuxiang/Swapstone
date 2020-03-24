from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .load_csv_data import load_csv_data
from .allocation import allocate
from django.contrib.auth.decorators import login_required
from .models import Booth, Map
from django.core import serializers


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
		map = load_csv_data(uploaded_file_url,request)
		booths = Booth.objects.filter(saved_map = map)
		allocate(booths)
		return render(request, 'capstone/home.html')
	return render(request, 'capstone/csv.html')

