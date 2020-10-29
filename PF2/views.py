from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import News, RegistrationData
from .forms import RegistrationForm, RegistrationModel
from django.contrib import messages

def Home(request):

    context = {
        "name": "PF",
        "number": 7777
    }

    return render(request, 'home.html', context)

def Newsp(request):
    obj = News.objects.get(id=1)
    """
    context={
       
        "list" : ["P", "j", "C3"],
        "mynum": 70#50
    }"""

    context={
        "data" : obj
    }

    return render(request, 'news.html', context)

def SportNews(request):
    return HttpResponse("<h1>SportNews</h1>")

def Contact(request):
    return render(request, 'contact.html')

def NewsDate(request, year):

    article_list = News.objects.filter(pub_date__year = year)

    context = {
        "year":year,
        "article_list":article_list
    }

    return render(request, 'newsdate.html', context)

def register(request):
    context = {
        "form":RegistrationForm
    }

    return render(request, 'signup.html', context)

def addUser(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        myregister = RegistrationData(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'],
                                    email=form.cleaned_data['email'],
                                    phone=form.cleaned_data['phone'])

        myregister.save()
        messages.add_message(request, messages.SUCCESS, "You have sign up successfully")


        #return redirect('home')
        return redirect('register')

def modelform(request):
    context = {
        "modelform" : RegistrationModel
    }
    return render(request, 'modal.html', context)

def addModelForm(request):
    mymodelform = RegistrationModel(request.POST)

    if mymodelform.is_valid():
        mymodelform.save()

    return redirect('model')
