from django.shortcuts import render ,redirect ,get_object_or_404
from .models import Tweets
from .forms import TweetForm , UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def tweet_list(request):
    tweets = Tweets.objects.all()
    return render(request,'tweetapp/tweetList.html',{'tweets':tweets})

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
        return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request,'tweetapp/tweetCreate.html',{'form':form})


@login_required
def tweet_edit(request,tweet_id):
    tweet = get_object_or_404(Tweets,id=tweet_id,user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
        return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request,'tweetapp/tweetEdit.html',{'form':form})


@login_required
def tweet_delete(request,tweet_id):
    tweet= get_object_or_404(Tweets,id=tweet_id,user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweetapp/tweetDelete.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user) 
            return redirect('tweet_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def user_logout(request):
    auth_logout(request)  # ✅ Use `auth_logout` instead of `logout`
    return redirect('login')