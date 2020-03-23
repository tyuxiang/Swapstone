from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .load_csv_data import load_csv_data
from .allocation import allocate


# Create your views here.
def home(request):
    return render(request, 'capstone/home.html')
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
		load_csv_data(uploaded_file_url)
		allocate()
		return render(request, 'capstone/csv.html')
	return render(request, 'capstone/csv.html')
	#return render(request, 'capstone/csv.html')

