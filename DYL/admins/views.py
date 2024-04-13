from admins.imports import *
from admins.distAdmin import *
today = datetime.date.today()

@login_required
def adminpage(request):
    userId = request.user.id
    who = Account.objects.get(id=userId)
    whom =who.name
    today = datetime.date.today()
    if who.type == 'CENTRE':
        forms = MarkForm()
        if request.method == 'POST':
            form = MarkForm(request.POST)
            if form.is_valid():
                frm = form.save(commit=False)
                try:
                    existence =approved.objects.filter(dylnumber=frm.dylnumber).count()
                    if existence>0:
                        patientdt = approved.objects.get(dylnumber=frm.dylnumber)
                        if (frm.dylnumber.upper()==patientdt.dylnumber and frm.otp.upper()==patientdt.otp and int(patientdt.dylrem)>0):
                            frm.centre=whom
                            frm.dyldone = datetime.datetime.now().replace(microsecond=0)
                            otpcheck = 0
                            while (otpcheck == 0):
                                otpcheck = get_random_string(length=5, allowed_chars='ABCDEFGHJKMNPQRSTUVWXYZ23456789')
                                if approved.objects.filter(otp=otpcheck).exists():
                                    otpcheck = 0
                            patientdt.otp = otpcheck
                            dylminus=int(patientdt.dylrem)
                            patientdt.dylrem=dylminus-1
                            patientdt.save()
                            if patientdt.dylrem==0:
                                patientdt.otp = "All Completed"
                                message2 = ('Dialysis Registration No: ' + str(patientdt.dylnumber) + ' has been successfully completed all coupons.%0A%0ASKSSF KANNUR')
                                a = SmsSent(message2, patientdt.phone,peid='1201161554659928564',teid='1207162954054980000')
                            else:
                                message2 = ('Dialysis Registration No: ' + str(patientdt.dylnumber) + ' Next Coupon Code: ' + str(patientdt.otp) + ' Coupon Remaining: ' + str(patientdt.dylrem)+'.%0A%0ASKSSF KANNUR')
                                a = SmsSent(message2,patientdt.phone,peid='1201161554659928564',teid='1207162954045572365')
                            frm.save()
                            messages.success(request, "Dialysis Marked")
                            return redirect('dashboard')
                        else:
                            messages.error(request, "Sorry, Details provided are not matching")
                            redirect('dashboard')
                    else:
                        messages.error(request, "Sorry, No Patient with Registration number as : "+frm.dylnumber)
                        redirect('dashboard')
                except():
                    messages.error(request, "Sorry, Details provided are not matching")
                    redirect('dashboard')
        pend = approved.objects.filter(centre=whom).exclude(dylrem=0)
        return render(request, 'centre.html',{'pending':pend,'whom':whom,'form':forms})

    elif who.type == 'CLUSTER':
        pending = patient.objects.filter(cluster=who.name,unit_approve='APPROVED', cluster_approve='PENDING')
        return render(request, 'cluster.html', {'pending': pending, 'whom':whom})

    elif who.type == 'MEDSHOP':
        pending = medicine.objects.filter(medshop=whom).exclude(dist_approve="FINISHED")
        return render(request, 'medical.html', {'pending': pending, 'whom':whom})

    elif who.type == 'ZONE':
        pending = patient.objects.filter(zone=who.name, unit_approve='APPROVED',cluster_approve='APPROVED',zonal_approve='PENDING')
        return render(request, 'zone.html', {'pending': pending, 'whom':whom})
    elif who.type == 'DIST':
        pending = patient.objects.filter(unit_approve='APPROVED', cluster_approve='APPROVED',
                                         zonal_approve='APPROVED').exclude(dist_approve='APPROVED').exclude(dist_approve='REJECTED')
        return render(request, 'dist.html', {'pending': pending, 'whom':whom})

    elif who.type == 'UNIT':
        pending = patient.objects.filter(unit=who.name, unit_approve='PENDING')
        return render(request, 'unit.html', {'pending': pending, 'whom':whom})



@login_required
def meddone(request):
    userId = request.user.id
    who = Account.objects.get(id=userId)
    whom = who.name
    if request.method=='POST':
        forms = MarkMedForm()
        if request.method == 'POST':
            form = MarkMedForm(request.POST)
            if form.is_valid():
                frm = form.save(commit=False)
                frm.centre = whom
                try:
                    existence = medicine.objects.filter(mdcnumber=frm.dylnumber.upper()).count()
                    if existence>0:
                        patientdt = medicine.objects.get(mdcnumber=frm.dylnumber.upper())
                        if (frm.otp.upper() == patientdt.otp1):
                            if patientdt.otp1 == "NA":
                                messages.error(request,"Not Available")
                                return redirect('dashboard')
                            else:
                                medremint = int(patientdt.medrem)
                                medremint = medremint - 1
                                patientdt.medrem = medremint
                                if medremint == 0:
                                    patientdt.dist_approve = "FINISHED"
                                patientdt.otp1="NA"
                                patientdt.save()
                            frm.dyldone = datetime.datetime.now().replace(microsecond=0)
                            frm.save()
                            messages.success(request, "Medicine Marked")
                            return redirect('dashboard')
                        elif(frm.otp.upper()==patientdt.otp2):
                            if patientdt.otp2 == "NA":
                                messages.error(request,"Not Available")
                                return redirect('dashboard')
                            else:
                                medremint = int(patientdt.medrem)
                                medremint = medremint - 1
                                patientdt.medrem = medremint
                                if medremint == 0:
                                    patientdt.dist_approve = "FINISHED"
                                patientdt.otp2="NA"
                                patientdt.save()
                            frm.dyldone = datetime.datetime.now().replace(microsecond=0)
                            frm.save()
                            messages.success(request, "Medicine Marked")
                            return redirect('dashboard')
                        elif(frm.otp.upper()==patientdt.otp3):
                            if patientdt.otp3 == "NA":
                                messages.error(request,"Not Available")
                                return redirect('dashboard')
                            else:
                                medremint = int(patientdt.medrem)
                                medremint = medremint - 1
                                patientdt.medrem = medremint
                                if medremint == 0:
                                    patientdt.dist_approve = "FINISHED"
                                patientdt.otp3="NA"
                                patientdt.save()
                            frm.dyldone = datetime.datetime.now().replace(microsecond=0)
                            frm.save()
                            messages.success(request, "Medicine Marked")
                            return redirect('dashboard')
                        elif(frm.otp.upper()==patientdt.otp4):
                            if patientdt.otp4 == "NA":
                                messages.error(request,"Not Available")
                                return redirect('dashboard')
                            else:
                                medremint = int(patientdt.medrem)
                                medremint = medremint - 1
                                patientdt.medrem = medremint
                                if medremint == 0:
                                    patientdt.dist_approve = "FINISHED"
                                patientdt.otp4="NA"
                                patientdt.save()
                            frm.dyldone = datetime.datetime.now().replace(microsecond=0)
                            frm.save()
                            messages.success(request, "Medicine Marked")
                            return redirect('dashboard')
                        else:
                            messages.error(request, "OTP Wrong")
                            return redirect('dashboard')

                    else:
                        messages.error(request, "Sorry, No Patient with Registration number as : "+frm.dylnumber)
                        redirect('dashboard')
                except():
                    messages.error(request, "Sorry, Something Went Wrong ")
                    redirect('dashboard')
        pend = medicine.objects.filter(medshop=whom)
        return render(request, 'medical.html',{'pending':pend,'whom':whom,'form':forms})

@login_required
def approvd(request):
    userId = request.user.id
    who = Account.objects.get(id=userId)
    whom = who.name
    if who.type == 'CENTRE':

        if request.method == 'POST':
            # pending = centre.objects.filter(centre=whom,dyldone__year=today.year,  dyldone__month=today.month)

            pending = centre.objects.filter(centre=whom, date__range=["2021-11-11", "2021-12-12"])
            return render(request, 'medicalapp.html', {'pending': pending, 'whom': whom})
        app = centre.objects.filter(centre=whom)
        return render(request, 'centreapp.html',{'app':app,'whom':whom})
    elif who.type == 'CLUSTER':
        pending = patient.objects.filter(cluster=who.name, cluster_approve='APPROVED',applytime__year=today.year, applytime__month=today.month)
        return render(request, 'clusterapp.html', {'pending': pending, 'whom':whom})
    elif who.type == 'MEDSHOP':
        if request.method == 'POST':
            if(request.POST.get('type')=='date'):
                pending = centre.objects.filter(centre=whom, dyldone__range=[request.POST.get('start'), request.POST.get('end')])
            else:
                pending = centre.objects.filter(centre=whom,dyldone__year=today.year,  dyldone__month=today.month)
            return render(request, 'medicalapp.html', {'pending': pending, 'whom': whom})
        pending = centre.objects.filter(centre=whom)
        return render(request, 'medicalapp.html', {'pending': pending, 'whom':whom})

    elif who.type == 'ZONE':
        pending = patient.objects.filter(zone=who.name, zonal_approve='APPROVED',applytime__year=today.year, applytime__month=today.month)
        return render(request, 'zoneapp.html', {'pending': pending, 'whom':whom})
    elif who.type == 'DIST':
        pending = patient.objects.filter(dist_approve='APPROVED')
        otpget = approved.objects.all()
        return render(request, 'distapp.html', {'pending': pending, 'whom':whom,'otpget':otpget})
    else:
        pending = patient.objects.filter(unit=who.name, unit_approve='APPROVED')
        return render(request, 'unitapp.html', {'pending': pending, 'whom':whom})

@login_required
def medapprov(request):
    pending = medicine.objects.filter(dist_approve='APPROVED')
    userId = request.user.id
    who = Account.objects.get(id=userId)
    whom = who.name
    if who.type == "DIST":
        return render(request, 'distmedapp.html', {'pending': pending, 'whom': whom})
    else:
        return redirect('dashboard')

@login_required
def refresh(request):
    userId = request.user.id
    who = Account.objects.get(id=userId)
    whom = who.name
    if who.type == 'DIST':
        today = datetime.date.today()
        objs = medicine.objects.filter(dist_approve="APPROVED").exclude(dateofreq__year=today.year, dateofreq__month=today.month)
        for item in objs:
            item.dist_approve = "FINISHED"
            item.save()
        messages.success(request, "Data Refreshed Except Current Month")
        return redirect('dashboard')
    return redirect('dashboard')

@login_required
def allpend(request):
    userId = request.user.id
    who = Account.objects.get(id=userId)
    whom = who.name
    if who.type == 'DIST':
        today = datetime.date.today()
        pending = patient.objects.all()
        return render(request, 'distallpend.html', {'pending': pending, 'whom': whom})

    else:
        return redirect('dashboard')

@login_required
def uapprove(request, data_id):
    if request.method == 'POST':
        obj = patient.objects.get(id=data_id)
        userId = request.user.id
        who = Account.objects.get(id=userId)
        if who.type == 'UNIT':
            obj.unit_approve = 'APPROVED'
            obj.unit_time = datetime.datetime.now().replace(microsecond=0)
            obj.save()
            cluster = Account.objects.get(name=obj.cluster, unit="NULL")
            message2 = 'An application has been approved by ' + obj.unit + ' with Application No: ' + obj.dylnumber + ' .Kindly Approve/Reject.%0A%0ASKSSF KANNUR'
            a=SmsSent(message2,cluster.phone,peid='1201161554659928564',teid='1207162954061975277')
            messages.success(request, "Approved Successfully")

        elif who.type == 'CLUSTER':
            obj.cluster_approve = 'APPROVED'
            obj.cluster_time = datetime.datetime.now().replace(microsecond=0)
            obj.save()
            zone = Account.objects.get(name=obj.zone, unit="NULL", cluster="NULL")
            message2 = 'An application has been approved by ' + obj.cluster + ' with Application No: ' + obj.dylnumber + ' .Kindly Approve/Reject.%0A%0ASKSSF KANNUR'
            a =SmsSent(message2,zone.phone,peid='1201161554659928564',teid='1207162954061975277')
            messages.success(request, "Approved Successfully")

        elif who.type == 'ZONE':
            obj.zonal_approve = 'APPROVED'
            obj.zonal_time = datetime.datetime.now().replace(microsecond=0)
            obj.save()
            message2 = 'An application has been approved by ' + obj.zone + ' with Application No: ' + obj.dylnumber + ' .Kindly Approve/Reject.%0A%0ASKSSF KANNUR'
            a = SmsSent(message2, str(9656154460),peid='1201161554659928564',teid='1207162954061975277')
            messages.success(request, "Approved Successfully")

        else:
           messages.error(request, "Something Went Wrong")
        return redirect('dashboard')
    return render(request,'../../KANNUR/DYL/templates/home.html')

@login_required
def ureject(request, data_id):
    if request.method == 'POST':
        obj = patient.objects.get(id=data_id)
        userId = request.user.id
        who = Account.objects.get(id=userId)
        if who.type == 'UNIT':
            obj.unit_approve = 'REJECTED'
            obj.unit_time = datetime.datetime.now().replace(microsecond=0)
            obj.save()
            messages.success(request, "Rejected Successfully")

        elif who.type == 'CLUSTER':
            obj.cluster_approve = 'REJECTED'
            obj.cluster_time = datetime.datetime.now().replace(microsecond=0)
            obj.save()
            messages.success(request, "Rejected Successfully")

        elif who.type == 'ZONE':
            obj.zonal_approve = 'REJECTED'
            obj.zonal_time = datetime.datetime.now().replace(microsecond=0)
            obj.save()
            messages.success(request, "Rejected Successfully")

        elif who.type == 'DIST':
            obj.dist_approve = 'REJECTED'
            obj.dist_time = datetime.datetime.now().replace(microsecond=0)

            obj.save()
            messages.success(request, "Rejected Successfully")

        else:
            messages.error(request, "Something Went Wrong")
            return redirect('dashboard')
        return redirect('dashboard')
    messages.error(request, "Something Went Wrong")
    return redirect('dashboard')

@login_required
def portreset(request,data_id):
    userId = request.user.id
    who = Account.objects.get(id=userId)
    if who.type == 'DIST':
        if request.method=='POST':
            obj =Account.objects.get(id=data_id)
            passw=int(obj.username)*78
            obj.password=make_password(str(passw))
            obj.save()
            messages.success(request, "Portal Reset Successfully")
            return redirect('dashboard')
    else:
        return redirect('dashboard')
@login_required
def portdel(request,data_id):
    userId = request.user.id
    who = Account.objects.get(id=userId)
    if who.type == 'DIST':
        if request.method=='POST':
            dele =Account.objects.get(id=data_id)
            dele.delete()
            messages.success(request, "Portal Deleted Successfully")
            return redirect('dashboard')
    else:
        return redirect('dashboard')













@login_required()
def unitrel(request,data_id):
    form =RelationForm()
    obj = patient.objects.get(id=data_id)
    if request.method=='POST':
        form = RelationForm(request.POST)
        if form.is_valid():
            frm=form.save(commit=False)
            obj.unit_relate = frm.unit_relate
            obj.save()
            messages.success(request, "Relation Added Successfully")
            return redirect('dashboard')
    return render(request, 'unitrel.html', {'obj': obj, 'form': form})

@login_required()
def unitmed(request):
    form = MedicalForm()
    userId = request.user.id
    who = Account.objects.get(id=userId)
    whom = who.name
    if medicine.objects.filter(unit=who.name, dist_approve="APPROVED").exists():
        obj = medicine.objects.get(unit=who.name, dist_approve="APPROVED")
        if datetime.date.today() < obj.lastdat:
            msg = "Coupon available till "+str(obj.lastdat)
        else:
            
            obj.dist_approve="FINISHED"
            obj.save()
            msg = ""

    elif medicine.objects.filter(unit=who.name, dist_approve="PENDING").exists():
        msg = "Already Applied for This Month"
    else :
        msg = ""
    if request.method=='POST':
        form = MedicalForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            lastmd = medicine.objects.filter().order_by('-id')[0]
            numbers = lastmd.mdcnumber.split('MDC')
            mdcno =int(numbers[1])
            obj.mdcnumber = ("MDC" + str(mdcno + 1))
            obj.unit = whom
            obj.dateofreq = datetime.datetime.now().replace(microsecond=0)
            obj.cluster = who.cluster
            obj.zone = who.zone
            obj.dist_approve="PENDING"
            obj.save()
            messages.success(request, "Medicine Applied Successfully")
            msg = "Application for Medicine is submitted successfully. Application Number: " + obj.mdcnumber + " Contact 9656154460 for more details.%0A%0ASKSSF KANNUR"
            a = SmsSent(msg, who.phone,peid='1201161554659928564',teid='1207162954048402621')
            return redirect('dashboard')
    return  render(request,'unitmed.html',{'form':form, 'whom':whom, 'msg':msg})

@login_required()
def unitmedapp(request):
    userId = request.user.id
    who = Account.objects.get(id=userId)
    whom =who.name
    if medicine.objects.filter(unit=who.name).exists():
        obj = medicine.objects.filter(unit=who.name).order_by('-id')
        return render(request, 'unitmedapp.html', {'obj': obj, 'whom': whom})
    return render(request, 'unitmedapp.html', {'whom': whom})


@login_required()
def otpcheck(request,data_id):
    pat = patient.objects.get(id=data_id)
    apprch = approved.objects.filter(dylnumber=pat.dylnumber).count()
    if apprch == 0:
        messages.info(request, "Patient is not approved")
    else:
        dylpat = approved.objects.get(dylnumber=pat.dylnumber)
        messages.info(request, "Coupon Code of " + dylpat.dylnumber + " : " + dylpat.otp)
    return redirect('approved')


@login_required
def dylcentrerep(request,data_id):
        centrename = Account.objects.get(id=data_id)
        donecountall = 0
        pendcountall = 0
        donemonthly = 0

        userId = request.user.id
        who = Account.objects.get(id=userId)
        if who.type == 'DIST':
            if centrename.type=="CENTRE":
                donecountall = centre.objects.filter(centre=centrename.name).count()
                donemonthly = centre.objects.filter(centre=centrename.name,dyldone__year=today.year,dyldone__month=today.month).count()
                pend = approved.objects.filter(centre=centrename.name)

                for jkj in pend:
                    conv = int(jkj.dylrem)
                    pendcountall+=conv
                return render(request, 'distdylrep.html', {'centrename': centrename.name, 'done': donecountall, 'pend': pendcountall, 'monthly':donemonthly})
            elif centrename.type=="MEDSHOP":
                donecountall = centre.objects.filter(centre=centrename.name).count()
                donemonthly = centre.objects.filter(centre=centrename.name, dyldone__year=today.year,
                                                       dyldone__month=today.month).count()
                amountobj=centre.objects.filter(centre=centrename.name, dyldone__year=today.year,
                                                       dyldone__month=today.month)
                amount =0
                for i in amountobj:
                    amount = amount + float(i.amount)
                pend = medicine.objects.filter(medshop=centrename.name)
                for k in pend:
                    conv = int(k.medrem)
                    pendcountall+=conv
                return render(request, 'distdylrep.html', {'centrename': centrename.name, 'done': donecountall, 'pend': pendcountall, 'monthly':donemonthly,'amount':amount})
            return redirect('dashboard')
        else:
            return redirect('dashboard')

@login_required()
def dylpat(request):
    today = datetime.date.today()
    dylpatient = approved.objects.all()
    userId = request.user.id
    who = Account.objects.get(id=userId)
    if who.type == 'DIST':
        return render(request, 'distdylrepsingle.html', {'dylpatient': dylpatient})
    else:
        return redirect('dashboard')
@login_required()
def dylrep(request):
    centres = Account.objects.filter(type="CENTRE")
    dylpatient = approved.objects.all()
    medical = Account.objects.filter(type="MEDSHOP")
    userId = request.user.id
    who = Account.objects.get(id=userId)
    if who.type == 'DIST':
        return render(request,'distrep.html',{'centres':centres,'dylpatient':dylpatient,'medical':medical})
    else:
        return redirect('dashboard')
def home(request):
   # values = Account.objects.all().exclude(is_admin=1)
    #for val in values:
     #   pw = val.password
      #  val.password = make_password(pw)
       # val.save()
    return redirect('dashboard')

@login_required
def delete(request,mem_id):
    userId = request.user.id
    who = Account.objects.get(id=userId)
    if request.method == 'POST':
        obj = medicine.objects.get(id=mem_id)
        obj.dist_approve = "DELETED"
        obj.save()
        messages.success(request, "Medicine Application Removed Successfully")
        return redirect('dashboard')


def couponMaker(type):
    otp_list = ['NA', 'NA', 'NA', 'NA']
    def randString():
        return get_random_string(length=4, allowed_chars='ABCDEFGHJKLMNPQRSTUVWXYZ')
    if type == '1':
        while(1):
            j = randString()
            k ='20'+j
            if k not in otp_list or medicine.objects.filter(otp1=j).exists() or medicine.objects.filter(otp2=j).exists() or medicine.objects.filter(otp3=j).exists() or medicine.objects.filter(otp4=j).exists():
                break
        otp_list[0]=k
    elif type == '2':
        pointer=0
        while (1):
            j = randString()
            k = '10' + j
            if k not in otp_list or medicine.objects.filter(otp1=j).exists() or medicine.objects.filter(otp2=j).exists() or medicine.objects.filter(otp3=j).exists() or medicine.objects.filter(otp4=j).exists():
                otp_list[pointer] = k
                pointer=pointer+1
            if pointer==2:
                break
    elif type == '3':
        pointer=0
        while (1):
            j = randString()
            if pointer==0:
                k = '10' + j
            else:
                k = '5' + j
            if k not in otp_list or medicine.objects.filter(otp1=j).exists() or medicine.objects.filter(otp2=j).exists() or medicine.objects.filter(otp3=j).exists() or medicine.objects.filter(otp4=j).exists():
                otp_list[pointer] = k
                pointer=pointer+1
                if pointer==3:
                    break
    elif type == '4':
        pointer = 0
        while (1):
            j = randString()
            k = '5' + j
            if k not in otp_list or medicine.objects.filter(otp1=j).exists() or medicine.objects.filter(otp2=j).exists() or medicine.objects.filter(otp3=j).exists() or medicine.objects.filter(otp4=j).exists():
                otp_list[pointer] = k
                pointer = pointer + 1
                if pointer == 4:
                    break
    elif type == '5':
        pointer = 0
        while (1):
            j = randString()
            if pointer == 0:
                k = '15' + j
            else:
                k = '5' + j
            if k not in otp_list or medicine.objects.filter(otp1=j).exists() or medicine.objects.filter(
                    otp2=j).exists() or medicine.objects.filter(otp3=j).exists() or medicine.objects.filter(
                    otp4=j).exists():
                otp_list[pointer] = k
                pointer = pointer + 1
                if pointer == 2:
                    break

    return otp_list
