from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'capstone/home.html')
def login(request):
	return render(request, 'capstone/login_page.html')
def logout(request):
	return render(request, 'capstone/logout.html')
def csv(request):
	return render(request, 'capstone/csv.html')