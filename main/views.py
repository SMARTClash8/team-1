from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import Links
from .test import save_photo

def index(request):
	if request.method == 'POST':
		form = UserForm(request.POST, request.FILES)
 
		if form.is_valid():
			form.save()
			# return redirect('success')
	else:
		form = UserForm()
	return render(request, 'main/index.html', {'form': form})

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
