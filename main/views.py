from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import Links
from .test import save_photo
from utils.module_model import model_loader, image_classify, get_photo_path

model_path = ("C:/Users/kuzik/Desktop/project3/models/model_from_Susana.h5", 
			  "C:/Users/kuzik/Desktop/project3/models/weights_from_Susana.h5")
model = model_loader(model_path)

def index(request):
	if request.method == 'POST':
		form = UserForm(request.POST, request.FILES)
 
		if form.is_valid():
			x = form.save()
			print(x)
			result = image_classify(get_photo_path(), 'si_rescale', model)
			print(result)
	else:
		form = UserForm()
	return render(request, 'html/index.html', {'form': form})

def success(request):
	return HttpResponse('successfully uploaded')

	# news = Links.objects.all()
	# if request.method == "POST":
	# 	form = UserForm(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# print(f"\n\n {news[13]} \n\n")
	# save_photo(news[21])


	# form = UserForm()
	# data = {
	# 	'form': form,
	# 	'news': news
	# }
	# return render(request, 'html/index.html', data)
