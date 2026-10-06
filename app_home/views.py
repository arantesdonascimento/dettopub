from django.shortcuts import render, redirect




def BASE(request):
    return render(request, 'base.html')



def home(request):
	context = {

	}

	return render(request, 'app_home/index.html', context)



def about(request):
	context = {

	}

	return render(request, 'app_home/about.html', context)



def contact(request):
	context = {

	}

	return render(request, 'app_home/contact.html', context)



def teremberles(request):
	context = {

	}

	return render(request, 'app_home/teremberles.html', context)


def esemenyek(request):
	context = {

	}

	return render(request, 'app_home/esemenyek.html', context)



def gallery(request):
	context = {

	}

	return render(request, 'app_home/gallery.html', context)



def pricing(request):
	context = {

	}

	return render(request, 'app_home/pricing.html', context)





