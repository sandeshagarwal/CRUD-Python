from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from enroll.forms import StudentRegistration
from enroll.models import User

# Create your views here.
# This function will add and show new items
def add_show(request):
    #return HttpResponse("Hello !") will check later
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            #fm.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all() # This will print all the dbaseata from the data
    return render(request, 'enroll\\addandshow.html',{'form':fm, 'stu':stud})

    #This function will delete the data
def delete_data(request,id):
    if request.method == 'POST': #pk is primary key
        d = User.objects.get(pk=id)
        d.delete()
        return HttpResponseRedirect('/')

# This function will update
def update_data(request,id):
    if request.method == 'POST':
        u = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=u)
        if fm.is_valid():
            fm.save()
    else:
        u = User.objects.get(pk=id)
        fm = StudentRegistration(instance=u)

    return render(request,'enroll/updatestudent.html',{'form':fm})