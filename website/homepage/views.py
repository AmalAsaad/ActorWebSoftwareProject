from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.shortcuts import redirect
from django.contrib import auth


# Create your views here.
# def homepage(request):
#    return render(request, 'contact.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message=Contact()
            message.user = auth.get_user(request)
            message.content = form.cleaned_data['message_area']
            message.save()
        return redirect('/actor/')

    else:
        form = ContactForm()
        return render(request,"contact.html",{"form":form})