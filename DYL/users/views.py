import datetime
import requests
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
# Users are the patients
from django.views.decorators.csrf import csrf_exempt

from admins.models import Account
from msg.views import SmsSent
from users.forms import PatientForm, ViewForm
from users.models import patient, approved

@csrf_exempt
def viewstat(request):
    form = ViewForm()
    if request.method == 'POST':
        form = ViewForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            reqstat = patient.objects.filter(dylnumber=obj.name,phone=obj.phone).count()
            if reqstat==0:
                messages.error(request,"No User Found with "+obj.name+" And "+obj.phone+" .")
            try:
                datas = patient.objects.get(dylnumber=obj.name,phone=obj.phone)
                unitno = Account.objects.get(unit=datas.unit,type='UNIT')
                clusterno = Account.objects.get(cluster=datas.cluster, unit='NULL',type='CLUSTER')
                zoneno = Account.objects.get(zone=datas.zone, cluster="NULL", unit='NULL',type='ZONE')

                if approved.objects.filter(dylnumber=obj.name).count()>0:
                    code = approved.objects.get(dylnumber=obj.name)
                    return render(request, 'success.html',
                                  {'data': datas, 'unitno': unitno, 'clusterno': clusterno, 'zoneno': zoneno,
                                   'code': code})
                else:
                    return render(request, 'success.html',
                                      {'data': datas, 'unitno': unitno, 'clusterno': clusterno, 'zoneno': zoneno})

            except (patient.DoesNotExist):
                error = "No Application Found"
                return render(request, 'status.html', {'form': form,'error':error})
    else:
        return render(request, 'status.html', {'form': form})
    return render(request, 'status.html', {'form': form})

def reg(request):
    unit = Account.objects.filter(type='UNIT')
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST,request.FILES)
        if form.is_valid():
            lastmd = patient.objects.filter().order_by('-id')[0]
            numbers = lastmd.dylnumber.split('DYL')
            dylno = int(numbers[1])
            obj=form.save(commit=False)
            unit = Account.objects.get(username=obj.unit)
            obj.unit = unit.unit
            obj.cluster = unit.cluster
            obj.zone = unit.zone
            obj.dylnumber = ("DYL"+ str(dylno+1))
            obj.applytime =datetime.datetime.now().replace(microsecond=0)
            obj.save()
            message1="Hello " + obj.name + " Your Dialysis Application No: " + obj.dylnumber + '. Kindly wait for the approval.%0A%0ASKSSF KANNUR'
            a = SmsSent(message1,obj.phone,peid='1201161554659928564',teid='1207162954041708193')
            
            message2 = 'An application has been submitted by ' + obj.name + ' with Application No:  ' +obj.dylnumber +'. Kindly Approve/Reject.%0A%0ASKSSF KANNUR'
            a = SmsSent(message2, obj.phone,peid='1201161554659928564',teid='1207162954051796959')
            try:
                datas = patient.objects.get(dylnumber=obj.dylnumber, phone=obj.phone)
                unitno = Account.objects.get(unit=datas.unit,type='UNIT')
                clusterno = Account.objects.get(cluster=datas.cluster, unit='NULL',type='CLUSTER')
                zoneno = Account.objects.get(zone=datas.zone, cluster="NULL", unit='NULL',type='ZONE')
                if approved.objects.filter(dylnumber=obj.dylnumber).count()>0:
                    code = approved.objects.get(dylnumber=obj.dylnumber)
                    return render(request, 'success.html',
                                  {'data': datas, 'unitno': unitno, 'clusterno': clusterno, 'zoneno': zoneno,
                                       'code': code})
                else:
                    return render(request, 'success.html',
                                      {'data': datas, 'unitno': unitno, 'clusterno': clusterno, 'zoneno': zoneno})

            except (patient.DoesNotExist):
                error = "No Application Found"
                return render(request, 'status.html', {'form': form, 'error': error,'unit':unit})
        else:

            return render(request, 'registration.html', {'form': form,'unit':unit})
    return render(request, 'registration.html', {'form': form,'unit':unit})
