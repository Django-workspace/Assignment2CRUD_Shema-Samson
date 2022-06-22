from pyexpat.errors import messages
from django.shortcuts import render

from populate.forms import traineeforms
from .models import assignment1,retrievedata
from django.contrib import messages

# Create your views here.
def homepage(request):
    if request.method=='POST':
        saverecord=assignment1()
        saverecord.fname=request.POST.get('fname')
        saverecord.lname=request.POST.get('lname')
        saverecord.save()
        messages.success(request, "Record Saved Successfully...")
    return render(request, 'homepage.html')

def showdata(request):
    resultdisp=retrievedata.objects.all()
    return render(request,"retrieve.html",{'retrievedata':resultdisp})

def deletedata(request, id):
    deldata=retrievedata.objects.get(id=id)
    deldata.delete()
    resultdisp=retrievedata.objects.all()
    return render(request,"retrieve.html",{'retrievedata':resultdisp})

def editdata(request,id):
    dispdata=retrievedata.objects.get(id=id)
    return render(request,"edit.html",{'retrievedata':dispdata})

def updatedata(request,id):
    updata=retrievedata.objects.get(id=id)
    form=traineeforms(request.POST,instance=updata)
    if form.is_valid():
        form.save()
        return render(request,"edit.html",{'retrievedata':updata})
