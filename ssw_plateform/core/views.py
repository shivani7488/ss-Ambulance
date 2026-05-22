from django.shortcuts import render, redirect
from .models import MusicPost, UserProfile
from django.contrib.auth.models import User

def home(request):
    recent_posts = MusicPost.objects.all().order_by('-created_at')[:5]
    context = {
        'posts': recent_posts
    }
    return render(request, 'home.html', context)

def profile(request):
    
    if not request.user.is_authenticated:
        user = User.objects.first() 
    else:
        user = request.user
    
    if request.method == 'POST':
        title = request.POST.get('title')
        lyrics = request.POST.get('lyrics')
        audio_file = request.FILES.get('audio_file') # Files ke liye request.FILES zaroori hai

        if title: 
            MusicPost.objects.create(
                user=user,
                title=title,
                lyrics=lyrics,
                audio_file=audio_file
            )
            return redirect('profile') 

    my_posts = MusicPost.objects.filter(user=user).order_by('-created_at')

    context = {
        'my_posts': my_posts,
        'current_user': user
    }
    return render(request, 'profile.html', context)