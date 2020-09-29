from django.shortcuts import render, redirect
from .form import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users,admin_only

def index(request):
    felul_principal = Principal.objects.all()
    bauturi = Bauturi.objects.all()
    desert = Desert.objects.all()

    context={'felul_principal':felul_principal,'bauturi':bauturi,
            'desert':desert}
    return render(request,'Digital/index.html',context)


def loginPage(request):
     if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,
                            password = password)
        if user is not None:
            login(request,user)
            return redirect('produse')

        else:
            messages.info(request,'username sau parola incorect')


     context = {}
     return render(request,'Digital/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def produse(request):

    return render(request, 'Digital/Dashboard.html')

# Felul Principal

@login_required(login_url='login')
def felul_principal(request):
    felul_principal = Principal.objects.all()
    context = {'felul_principal': felul_principal}
    return render(request, 'Digital/felul_principal.html',context)


@login_required(login_url='login')
def crearefelul_principal(request):
    form = principalForm()
    if request.method == "POST":
        form = principalForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('felul_principal')

    context = {'form':form}
    return render(request,'Digital/order_form.html',context)


@login_required(login_url='login')
def modificafelul_principal(request,pk):
    modificare = Principal.objects.get(id=pk)
    form = principalForm(instance=modificare)
    if request.method == 'POST':
        form = principalForm(request.POST,request.FILES,instance = modificare)
        if form.is_valid():
            form.save()
            return redirect('felul_principal')
    context={'form':form}
    return render(request, 'Digital/order_form.html', context)



@login_required(login_url='login')
def stergerefelul_principal(request,pk):
    stergere = Principal.objects.get(id=pk)
    if request.method == 'POST':
        stergere.delete()
        return redirect('felul_principal')
    context = {'stergere':stergere}
    return render(request, 'Digital/delete.html', context)




# Bauturi
@login_required(login_url='login')
def bauturi(request):
    bauturi = Bauturi.objects.all()
    context = {'bauturi': bauturi}
    return render(request, 'Digital/bauturi.html',context)



@login_required(login_url='login')
def crearebauturi(request):
    form = bauturiForm()
    if request.method == "POST":
        form = bauturiForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bauturi')

    context = {'form':form}
    return render(request,'Digital/order_form.html',context)



@login_required(login_url='login')
def modificabauturi(request,pk):
    modificare = Bauturi.objects.get(id=pk)
    form = bauturiForm(instance=modificare)
    if request.method == 'POST':
        form = bauturiForm(request.POST,request.FILES,instance = modificare)
        if form.is_valid():
            form.save()
            return redirect('bauturi')
    context={'form':form}
    return render(request, 'Digital/order_form.html', context)



@login_required(login_url='login')
def stergerebauturi(request,pk):
    stergere = Bauturi.objects.get(id=pk)
    if request.method == 'POST':
        stergere.delete()
        return redirect('bauturi')
    context = {'stergere':stergere}
    return render(request, 'Digital/delete.html', context)



# Desert
@login_required(login_url='login')
def desert(request):
    desert = Desert.objects.all()
    context = {'desert': desert}
    return render(request, 'Digital/desert.html',context)

def crearedesert(request):
    form = desertForm()
    if request.method == "POST":
        form = desertForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('desert')

    context = {'form':form}
    return render(request,'Digital/order_form.html',context)


@login_required(login_url='login')
def modificadesert(request,pk):
    modificare = Desert.objects.get(id=pk)
    form = desertForm(instance=modificare)
    if request.method == 'POST':
        form = bauturiForm(request.POST,request.FILES,instance = modificare)
        if form.is_valid():
            form.save()
            return redirect('desert')
    context={'form':form}
    return render(request, 'Digital/order_form.html', context)



@login_required(login_url='login')
def stergeredesert(request,pk):
    stergere = Bauturi.objects.get(id=pk)
    if request.method == 'POST':
        stergere.delete()
        return redirect('desert')
    context = {'stergere':stergere}
    return render(request, 'Digital/delete.html', context)
