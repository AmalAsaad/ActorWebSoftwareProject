from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Actor, ActorForm, Movie, Prize,Review
from django.shortcuts import redirect,render_to_response
from django.contrib.auth import login, authenticate
from django.views.generic import View
from .forms import UserFormRegister, UserFormEdit,ReviewForm,CommentForm,MessageForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm,UserCreationForm
from django.contrib.auth import update_session_auth_hash
from django import forms
from .models import Review,Message
from django.contrib import auth
from django.template.context_processors import csrf





# Create your views here.

def index(request):
    actors = Actor.objects.all()
    return render(request, 'actor/index.html', {"actors": actors})


def details(request, actor_id):
    actor = get_object_or_404(Actor, pk=actor_id)
    # actor = Actor.objects.get(id=actor_id)
    prizes = Prize.objects.filter(actor=actor)
    movies = Movie.objects.filter(actor=actor)
    reviews = Review.objects.filter(actor=actor)
    return render(request, "actor/details.html", {"actor": actor, "prizes": prizes, "movies": movies, "reviews":reviews})








def search(request):
    if request.method == 'POST':
        actorName = request.POST.get('search')
        try:
            actors = Actor.objects.filter(name__contains=actorName)
            # Add_prod class contains a column called 'bookname'
        except Actor.DoesNotExist:
            actors = None
        return render(request, "actor/search.html", {"actors": actors})
    else:
        return render(request, "actor/search.html", {})


def create(request):
    if request.method == 'GET':
        return render(request, "actor/create.html")
    else:
        actor = ActorForm(request.POST)
        actor.save()
        return redirect("index")


def edit(request, actor_id):
    if request.method == 'GET':
        actor = Actor.objects.get(id=actor_id)
        return render(request, "actor/edit.html", {"actor": actor})
    else:
        old = Actor.objects.get(id=actor_id)
        new = ActorForm(request.POST)
        old.name = new['name'].value()
        old.birthdate = new['birthdate'].value()
        old.socialMedia = new['socialMedia'].value()
        old.image = new['image'].value()
        old.save()
        return redirect('index')


def delete(request, actor_id):
    actor = Actor.objects.get(id=actor_id)
    actor.delete()
    return redirect("index")

def UserFormView(request):
    from_class = UserFormRegister
    template_name = "actor/registration.html"
    if request.method=='POST':
        form = from_class(request.POST)
        if form.is_valid():
             user = form.save()
            #user.refresh_from_db()  # load the profile instance created by the signal
            #user.userprofile.age = form.cleaned_data.get('age')
            #user.userprofile.country = form.cleaned_data.get('country')
            #user.userprofile.bio = form.cleaned_data.get('bio')
            #user.userprofile.img = form.cleaned_data.get('img')
             user.save()
             raw_password = form.cleaned_data.get('password1')
             user = authenticate(username=user.username, password=raw_password)
             login(request, user)
             return redirect('/actor/profile')
        #else:
          #  return HttpResponse("You have signed up before")

    else:
        form = from_class()
        return render(request,template_name,{"form":form})










def view_profile(request):
    if request.user.is_authenticated:
        return render(request, 'actor/profile.html', {"user": request.user})
    else:
        return redirect('/actor/login')


def edit_profile(request):
    if request.method == 'POST':
        form = UserFormEdit(request.POST, instance=request.user)
        if form.is_valid():
                form.save()
                return redirect('/actor/profile')

    else:
        form = UserFormEdit(instance=request.user)
        return render(request, 'actor/edit_profile.html', {"form": form})



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/actor/profile')
        else:
            return redirect('/actor/login')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'actor/change_password', {"form": form})







def review(request,actor_id):
    actor = get_object_or_404(Actor, pk=actor_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review=Review()
            review.user = auth.get_user(request)
            review.actor = actor
            review.description = form.cleaned_data['review_area']
            review.save()
        return redirect('/actor/')

    else:
        form = ReviewForm()
        return render(request,'actor/review.html',{"form":form, "actor":actor})


def message(request,actor_id):
    actor = get_object_or_404(Actor, pk=actor_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message=Message()
            message.user = auth.get_user(request)
            message.actor = actor
            message.content = form.cleaned_data['message_area']
            message.save()
        return redirect('/actor/')

    else:
        form = MessageForm()
        return render(request,'actor/message.html',{"form":form, "actor":actor})
