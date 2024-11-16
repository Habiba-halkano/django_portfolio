from django.shortcuts import render, redirect

from .forms import ContactForm


# Create your views here.
def index(request):
    return render(request,'base.html')

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('success')
    else:
            form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def projects(request):
    return render(request, 'projects.html')