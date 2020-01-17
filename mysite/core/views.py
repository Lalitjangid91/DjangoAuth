from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
def Home(request):
    count=User.objects.count()
    return render(request,'home.html',{'count':count})

def SignUp(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UserCreationForm()
    return render(request,'signup.html',{'form':form})
@login_required
def SecretPage(request):
    return render(request,'secretpage.html')

class SecretPage2(LoginRequiredMixin,TemplateView):
    template_name='secretpage.html'
