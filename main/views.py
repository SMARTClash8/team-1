from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import Links
from .test import save_photo
from .detete_all_files import delete_images
def index(request):
	# delete_images('./media/images')
	new = 122
	if request.method == 'POST':
		form = UserForm(request.POST, request.FILES)
		photo_name = str(request.FILES["link"])
		if photo_name[-4:] == 'jpeg' or photo_name[-4:] == 'jfif' or photo_name[-3:] == 'jpg':
			if form.is_valid():
				form.save()
				new = 124
				# return redirect('success')
		else:
			return HttpResponse('The photo format is not suitable')
	else:
		form = UserForm()
	return render(request, 'html/index.html', {'form': form, 'new': new})

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
