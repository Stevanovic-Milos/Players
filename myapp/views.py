from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils.dateparse import parse_date
from .models import Post
import os


# Home page
def index(request):
    posts = Post.objects.all().order_by("-id")
    return render(request, "index.html", {
        'posts': posts,
        'top_posts': Post.objects.all().order_by("-visina"),
        'user': request.user,
        'media_url': settings.MEDIA_URL  
    })


# User registration (signup)
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Korisničko ime već postoji")
                return redirect('signup')
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email već postoji")
                return redirect('signup')
            else:
                User.objects.create_user(username=username, email=email, password=password).save()
                return redirect('signin')
        else:
            messages.info(request, "Šifre moraju biti iste")
            return redirect('signup')
            
    return render(request, "signup.html")


# User login (signin)
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            messages.info(request, 'Korisničko ime ili šifra nisu ispravni')
            return redirect("signin")
            
    return render(request, "signin.html")


# User logout
@login_required
def logout(request):
    auth.logout(request)
    return redirect('index')


# Blog page
@login_required
def blog(request):
    return render(request, "index.html", {
        'posts': Post.objects.filter(user_id=request.user.id).order_by("-id"),
        'user': request.user,
        'media_url': settings.MEDIA_URL  # Ensure media_url is passed here as well
    })


# Create post
@login_required
def create(request):
    if request.method == 'POST':
        try:
            ime = request.POST.get('ime')
            prezime = request.POST.get('prezime')
            nedostaci = request.POST.get('nedostaci')
            prednosti = request.POST.get('prednosti')
            visina = request.POST.get('visina')
            tezina = request.POST.get('tezina')
            noga = request.POST.get('noga')
            pozicija = request.POST.get('pozicija')
            video_url = request.POST.get('video_url')
            image = request.FILES.get('image')
            datum_rođenja_str = request.POST.get('datum_rođenja')
            datum_rođenja = parse_date(datum_rođenja_str) if datum_rođenja_str else None

            post = Post(
                ime=ime,
                prezime=prezime,
                nedostaci=nedostaci,
                prednosti=prednosti,
                visina=visina,
                tezina=tezina,
                noga=noga,
                pozicija=pozicija,
                video_url=video_url,
                image=image,
                datum_rođenja=datum_rođenja,
                user=request.user
            )
            post.save()
            return redirect('index')
        except Exception as e:
            messages.error(request, f"Error creating post: {e}")
            return redirect('create')
    else:
        return render(request, "create.html")


# User profile page
@login_required
def profile(request, id):
    profile_user = get_object_or_404(User, id=id)
    return render(request, 'profile.html', {
        'profile_user': profile_user,
        'posts': Post.objects.filter(user_id=id),
        'media_url': settings.MEDIA_URL 
    })


# Edit profile page
@login_required
def profileedit(request, id):
    if request.user.id != id:
        messages.error(request, "You can only edit your own profile.")
        return redirect('profile', id=request.user.id)

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
    
        user = request.user
        user.first_name = firstname
        user.last_name = lastname
        user.email = email
        user.save()
        return redirect('profile', id=id)
    return render(request, "profileedit.html", {'user': request.user})


# Post details page
def post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "post-details.html", {
        'post': post,
        'recent_posts': Post.objects.all().order_by("-id"),
        'media_url': settings.MEDIA_URL  
    })


# Edit post
@login_required
def editpost(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user != post.user:
        messages.error(request, "You can only edit your own posts.")
        return redirect('profile', id=request.user.id)

    if request.method == 'POST':
        try:
            post.ime = request.POST.get('ime', post.ime)
            post.prezime = request.POST.get('prezime', post.prezime)
            post.nedostaci = request.POST.get('nedostaci', post.nedostaci)
            post.prednosti = request.POST.get('prednosti', post.prednosti)
            post.visina = request.POST.get('visina', post.visina)
            post.tezina = request.POST.get('tezina', post.tezina)
            post.noga = request.POST.get('noga', post.noga)
            post.pozicija = request.POST.get('pozicija', post.pozicija)
            post.video_url = request.POST.get('video_url', post.video_url)
            image = request.FILES.get('image', post.image)
            datum_rođenja_str = request.POST.get('datum_rođenja', None)
            datum_rođenja = parse_date(datum_rođenja_str) if datum_rođenja_str else post.datum_rođenja

            if image:
                post.image = image
            post.datum_rođenja = datum_rođenja
            post.save()
            return redirect('profile', id=request.user.id)
        except Exception as e:
            messages.error(request, f"Error updating post: {e}")
            return redirect('editpost', id=id)
    
    return render(request, "postedit.html", {'post': post})

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)

# Delete post
@login_required
def deletepost(request, id):
    post = get_object_or_404(Post, id=id)

    # Check if the logged-in user is the owner of the post
    if request.user != post.user:
        messages.error(request, "You can only delete your own posts.")
        return redirect('profile', id=request.user.id)

    # Delete image from AWS S3 (if the post has an image)
    if post.image:
        try:
            # Delete image from S3
            post.image.delete(save=False)  # Automatically deletes from S3 (if using django-storages)
        except Exception as e:
            messages.error(request, f"Error deleting image from AWS S3: {str(e)}")
            return redirect('profile', id=request.user.id)

    # Delete the post
    post.delete()

    # Redirect to the user's profile page
    return redirect('profile', id=request.user.id)