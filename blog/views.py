from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from .forms import (PostForm, CommentForm, ToContactForm, ProfileForm, ProfileUpdateForm)

from .models import (Post, Category,Comment, Profile, Sign_up)
# Create your views here.

def get_categories():
    all = Category.objects.all()
    count = all.count()
    return {'cat1':all[:count//2], "cat2":all[count//2:]}

def index(request):
    posts = Post.objects.all().order_by("-published_date")
    # postid = Post.objects.get(pk=1)
    # posts = Post.objects.filter(title__contains="Post")
    # posts = Post.objects.filter(published_date__year=2023)
    # posts = Post.objects.filter(category__name__iexact = "C++")

    context={ "posts": posts
    }
    context.update(get_categories())
    return render(request,'blog/index.html',context=context)

def post(request, id=None):
    post = get_object_or_404(Post, title=id)
    comment_form=CommentForm()
    comments = Comment.objects.filter(post=post)
    if request.method == "POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post=post
            comment.user=request.user
            comment.published_date=now()
            comment.save()
            return render(request,'blog/post.html',context={'post':post, 'comment_form':comment_form, 'comments':comments})

    context={'post':post,'comments': comments, 'comment_form':comment_form}
    context.update(get_categories())
    return render(request,'blog/post.html',context=context)



def about(request):

    context={

    }
    return render(request,'blog/about.html',context=context)

def contacts(request):
    if request.method == "POST":
        form=ToContactForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return index(request)
    form=ToContactForm()
    context={'form':form}
    context.update(get_categories())
    return render(request,'blog/contacts.html',context=context)
def services(request):

    context={

    }
    return render(request,'blog/services.html',context=context)
def category(request, name=None):
    c= get_object_or_404(Category,name=name)
    posts=Post.objects.filter(category=c).order_by('-published_date')
    context={'posts':posts}
    context.update(get_categories())
    return render(request,'blog/index.html',context=context)

def search(request):
    query=request.GET.get('query')
    posts = Post.objects.filter(Q(content__icontains=query) | Q(title__icontains=query)).order_by("-published_date")

    context = {"posts": posts
               }
    context.update(get_categories())
    return render(request, 'blog/index.html', context=context)


# def get_commentaries():
#     all = Comment.objects.all()
#     count = all.count()
#     return all

# def commentary(request, name=None):
    # com = get_object_or_404(Comment, name=name)
    # comments = Comment.objects.filter(post=com).order_by('-published_date')
    # context = {'comments': comments}
    # context.update(get_categories())
    # return render(request,'blog/index.html',context=context)
    # if request.method == "POST":
    #     form=CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.published_date=now()
    #         comment.save()
    #         return index(request)
    # form=CommentForm()
    # context={'form':form}
    # context.update(get_categories())
    # return render(request,'blog/post.html',context=context)


@login_required
def create(request):
    if request.method == "POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date=now()
            post.user=request.user
            post.save()
            return index(request)
    form=PostForm()
    context={'form':form}
    context.update(get_categories())
    return render(request,'blog/create.html',context=context)

def sign_up(request):
    if request.method == "POST":
        form=ProfileForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return index(request)
    form=ProfileForm()
    context={'form':form}
    context.update(get_categories())
    return render(request,'blog/sign_up.html',context=context)

@login_required
def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user, login=request.user.username, email=request.user.email, poster='https://i.pinimg.com/564x/92/c5/11/92c511eb998b41b3d6c78fc9522f5927.jpg', date_of_birth='2000-01-01T00:00:00Z')


    return render(request, 'blog/profile.html', {'profile': profile})




def update_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'blog/update_profile.html', {'form': form})


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_up')
    else:
        form = UserCreationForm()

    return render(request, 'blog/registration_user.html', {'form': form})