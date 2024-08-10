from django.shortcuts import render, HttpResponse, redirect
from .models import register, fileupload

# Create your views here.


def registerpage(request):
    if request.method == 'POST':
        getname = request.POST.get('name')
        getaddress = request.POST.get('address')
        getusername = request.POST.get('username')
        getpassword = request.POST.get('password')
        users = register()
        users.Name = getname
        users.Address = getaddress
        users.Username = getusername
        users.Password = getpassword
        users.save()
    return render(request, 'registerpage.html')

def userlog(request):
    if request.method == 'POST':
        getusername = request.POST.get('username')
        getpassword = request.POST.get('password')
        try:
            register.objects.get(Username=getusername, Password=getpassword)
            return HttpResponse('Welcome User')
        except:
            return HttpResponse('Invalid User')
    return render(request, 'userlogin.html')

def adminlog(request):
    if request.method == 'POST':
        getusername = request.POST.get('username')
        getpassword = request.POST.get('password')
        if getusername == 'admin' and getpassword == 'Stefy@0818':
            return HttpResponse('Welcome Admin')
        else:
            return HttpResponse('Invalid')
    return render(request,'adminlogin.html')

def adminhome(request):
    return render(request,'adminhome.html')

def pending(request):
    details = register.objects.filter(Status=False)
    return render(request, 'pendinglist.html', {'value': details})

def approve(request,id):
    data = register.objects.get(id=id)
    data.Status = True
    data.save()
    return redirect('/pending')

def approved(request):
    details = register.objects.filter(Status=True)
    return render(request,'approvedlist.html', {'value': details})

def operations(request):
    details = register.objects.all()
    return render(request,'operations.html',{'value': details})

def edit(request,id):
    details = register.objects.all()
    user_data = register.objects.get(id=id)
    if request.method == 'POST':
        getaddress = request.POST.get('address')
        getpassword = request.POST.get('password')
        user_data.Address = getaddress
        user_data.Password = getpassword
        user_data.save()
        return redirect('/operations')
    return render(request,'operations.html',{'value': details, 'data': user_data})

def delete(request,id):
    data = register.objects.get(id=id).delete()
    return redirect('/operations')

def upload(request):
    if request.method == 'POST':
        getname = request.POST.get('name')
        getmail = request.POST.get('mail')
        getdesignation = request.POST.get('designation')
        getpicture = request.FILES['picture']
        file = fileupload()
        file.Name = getname
        file.Mail = getmail
        file.Designation = getdesignation
        file.Picture = getpicture
        file.save()
    return render(request, 'uploadfile.html')

def imgview(request):
    details = fileupload.objects.all()
    return render(request,'viewimage.html',{'value': details})