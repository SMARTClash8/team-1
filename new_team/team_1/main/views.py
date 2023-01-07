from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .models import Links
from .test import save_photo
def index(request):
	news = Links.objects.all()
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
	print(f"\n\n {news[13]} \n\n")
	save_photo(news[21])


	form = UserForm()
	data = {
		'form': form,
		'news': news
	}
	return render(request, 'html/index.html', data)
