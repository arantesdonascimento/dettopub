from django.shortcuts import render, redirect




def blogs(request):
	context = {

	}

	return render(request, 'app_blog/blog.html', context)



def blog_details(request):
	context = {

	}

	return render(request, 'app_blog/blog_details.html', context)



def blog_create(request):
	context = {

	}

	return render(request, 'app_blog/blog_create.html', context)







