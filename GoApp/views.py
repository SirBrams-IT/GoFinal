from datetime import datetime

from django.db.models.fields import return_None
from django.shortcuts import render,redirect
from django.template.context_processors import request
from GoApp.models import Appointment,Contact,User
from GoApp.forms import AppointmentForm


# Create your views here.
def home(request):
    if request.method=='POST':
        if User.objects.filter(
            username= request.POST['username'],
            password=request.POST['password']
        ).exists():
            return  render(request,'index.html')
        else:
         return render(request,'login.html')


    else:
        return render(request,'login.html')






def service(request):
    return render(request,'service-details.html')
def starter(request):
    return render(request,'starter-page.html')
def about(request):
    return render(request,'about.html')
def doctors(request):
    return render(request,'doctors.html')
def services(request):
    return render(request,'service.html')


def appointment(request):
   if request.method=='POST':
      myappointments= Appointment(
           name= request.POST['name'],
           email= request.POST['email'],
           phone= request.POST['phone'] ,
           date=request.POST['date'],
           department=request.POST['department'],
           doctor=request.POST['doctor'],
           message=request.POST['message']

       )
      myappointments.save()
      return redirect('/appointment')

   else:
       return render(request,'appointment.html')

def contact(request):
   if request.method=='POST':
       mycontact = Contact(
           name = request.POST['name'],
           email = request.POST['email'],
           subject = request.POST['subject'],
           message = request.POST['message']
       )
       mycontact.save()
       return redirect('/record')

   else:
       return render(request,'contact.html')



def show(request):
    allappointments = Appointment.objects.all()
    return render(request,'show.html',{'appointment':allappointments})

def delete(request,id):
    appoint = Appointment.objects.get(id  = id )
    appoint.delete()
    return redirect('/show')

def record(request):
    myrecord = Contact.objects.all()
    return render(request,'record.html',{'record':myrecord})

def delete_record(request,id):
    mycontact= Contact.objects.get(id  = id )
    mycontact.delete()
    return redirect('/record')

def edit(request,id):
    editappointment = Appointment.objects.get(id=id)
    return render(request,'edit.html',{'appointment':editappointment})

def update(request,id):

    updateinfo = Appointment.objects.get(id =id)
    form = AppointmentForm(request.POST , instance = updateinfo)
    if form.is_valid():
     form.save()
     return redirect('/show')

    else:
     return render(request,'edit.html')

def register(request):
    if request.method=='POST':
      members = User(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password']
      )
      members.save()
      return redirect('/login')

    else:
        return render(request,'register.html')




def login(request):
    return render(request,'login.html')
