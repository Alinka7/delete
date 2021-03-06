from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post


def post_create(request,):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit = False)
		print(form.cleaned_data.get("title"))
		instance.save()
		messages.success(request, "successfully created")
		#MESSAGE SUCCESS
		return HttpResponseRedirect(instance.get_absolute_url())


	context = {
	"form":form,
	}
	return render(request, 'post_form.html',context)

def post_detail(request, id = None): #retreive
	#instance = Post.objects.get(id = 6)
	instance = get_object_or_404(Post, id = id)
	context = {
	"title": instance.title,
	"instance": instance,
	}
	return render(request, 'post_detail.html',context)
	 

def post_list(request): #list items 
	queryset_list = Post.objects.all()#.order_by("-timestamp")
	paginator = Paginator(queryset_list, 3) # Show 25 contacts per page.
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)


	context = {
	"object_list": queryset,
	"title": "List",
		}
	return render(request, 'post_list.html', context)

def post_update(request, id = None):
	instance = get_object_or_404(Post, id = id)
	form = PostForm(request.POST or None, request.FILES or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		messages.success(request, "<a href = '#'> Item </a>saved", extra_tags = "html_safe")
		#MESSAGE SUCCESS
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
	"title": instance.title,
	"instance": instance,
	"form": form,
	}
	return render(request, 'post_form.html',context)

def post_delete(request, id = None):
	instance = get_object_or_404(Post, id = id)
	instance.delete()
	messages.success(request, "successfully deleted")
	return redirect("posts: list")