from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .forms import UserForm
# from .models import Links
from .test import save_photo
from utils.module_model import model_loader, image_classify, get_photo_path
from .main_path import PATH_FOLDER_MODEL, PATH_FOLDER_PROJECT
from .detete_all_files import delete_images
from django.shortcuts import  render
from django.core.files.storage import FileSystemStorage
model_path = (PATH_FOLDER_MODEL + "model_from_Susana_v2.h5", 
			  PATH_FOLDER_MODEL + "weights_from_Susana_v2.h5")
model = model_loader(model_path)

def index(request):
	result = ''
	if request.method == 'POST':
		# form = UserForm(request.POST, request.FILES)
		delete_images('./media/images')
		# if form.is_valid():
		if request.method == 'POST' and request.FILES['upload']:
			upload = request.FILES['upload']
			fss = FileSystemStorage()
			file = fss.save(upload.name, upload)
			file_url = fss.url(file)
			# print(file)
			# print(file_url)
			# x = form.save()
			# full_name = PATH_FOLDER_PROJECT + "team_1/media/images/" + str(request.FILES['link'])
			result = image_classify((PATH_FOLDER_PROJECT+ "" +file_url), 'si_rescale', model)
			print(result)
			return render(request, 'html/index.html', {'result': result})
	return render(request, 'html/index.html')
	# else:
	# 	form = UserForm()
	# 	pass
	# return render(request, 'html/index.html', {'form': form, 'result': result})

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
