from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import Links
from .test import save_photo
from .detete_all_files import delete_images
def index(request):
	delete_images('./media/images')
	if request.method == 'POST':
		# delete_images('../media/images')
		form = UserForm(request.POST, request.FILES)
		photo_name = str(request.FILES["link"])
		print(photo_name)
		if form.is_valid():
			form.save()
			# return redirect('success')
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
