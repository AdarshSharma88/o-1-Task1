from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def hello_world(request):
	return HttpResponse("Hello World")

def home_page(request):
	context={
    "submitted":False
	}
	if(request.method=='POST'):
		context["submitted"]=True
		data = request.POST
		long_url = data['longurl']
		custom_name = data['custom_name']

		print(long_url)
		print(custom_name)
		#print(request.POST)

		context["long_url"]=long_url
		context["short_url"]=request.build_absolute_uri()+custom_name
	else:
		print("There is no data")
	
	
	return render(request,"index.html",context)

def task(request):
	context={
	"my_name":"Adarsh",
	"x":13
	}
	return render(request,"test.html",context)