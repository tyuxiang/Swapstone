from django.shortcuts import render
from .forms import UploadFileForm

# Create your views here.
def home(request):
    return render(request, 'capstone/home.html')
def login(request):
	return render(request, 'capstone/login_page.html')
def logout(request):
	return render(request, 'capstone/logout.html')

def csv(request):
	print("HI")
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['file'])
			print("File was uploaded successfully")
			return HttpResponseRedirect('/success/url/')
		else:
			print(form.errors)
	else:
		form = UploadFileForm()
	return render(request, 'capstone/csv.html', {'form': form})
	#return render(request, 'capstone/csv.html')
def handle_uploaded_file(f):
	for chunk in f.chunks():
		print(chunk)