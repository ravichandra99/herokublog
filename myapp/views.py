from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from myapp.models import Post
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
	posts = Post.objects.all()
	context = {'posts':posts}
	return render(request,'index.html',context)

class PostDetail(LoginRequiredMixin,DetailView):
	model = Post
	template_name = 'post_detail.html'

def like_view(request):
	if request.is_ajax():
		post_id = request.GET.get('post_id')
		likes = request.GET.get('likes')
		post = Post.objects.get(id = post_id)
		post.likes += 1
		post.save()
	result = {'likes':post.likes}
	return JsonResponse(result)