from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from . models import Post, Profile
from django.contrib.auth.models import User
from . forms import NewPostForm, UserForm, ProfileForm 
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import Post, Profile
from . serializer import PostSerializer,ProfileSerializer
import datetime as dt

@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user.id
    user = request.user
    date = dt.date.today()
    posts = Post.objects.all()
    if Profile.objects.filter(user = request.user).count() == 0:
        prof = Profile(user=request.user)
        prof.save()
    return render(request, 'index.html',{"date": date, "posts": posts})

@login_required(login_url='/accounts/login/')
def profile(request,user_id=None):
    if user_id == None:
        user_id=request.user.id
    current_user = User.objects.get(id = user_id)
    user = current_user
    images = Post.objects.filter(user=current_user)
    profile = Profile.objects.all()
    return render(request, 'profile.html', locals())

@login_required(login_url='/accounts/login')
def updateprofile(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return redirect('profile')

	else:
			form = ProfileForm()
	return render(request, 'updateprofile.html',{"form":form })

@login_required(login_url='/accounts/login/')
def vote(request,post_id):
    try:
        post = Post.objects.get(id = post_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"vote.html", {"post":post})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('index')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form":form})

def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_user(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"profile": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

class PostList(APIView):
    def get(self, request, format=None):
        all_post = Post.objects.all()
        serializers = PostSerializer(all_post, many=True)
        return Response(serializers.data)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Post.objects.all()
        serializers = PostSerializer(all_profile, many=True)
        return Response(serializers.data) 