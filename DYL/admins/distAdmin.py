from admins.imports import *
today = datetime.date.today()

@login_required
def medview(request):
    userId = request.user.id
    who = Account.objects.get(id=userId)
    whom = who.name
    today = datetime.date.today()
    if who.type == 'DIST':
        pending = medicine.objects.filter( dateofreq__year=today.year,dateofreq__month=today.month).exclude(dist_approve='APPROVED').exclude(dist_approve="FINISHED").exclude(dist_approve="REJECTED")
        return render(request, 'distmed.html', {'pending': pending, 'whom': whom})
    else:
        return redirect('dashboard')


@login_required
def viewedit(request):
    userId = request.user.id
    who = Account.objects.get(id=userId)
    whom = who.name
    if who.type == 'DIST':
        acc = Account.objects.all().exclude(type='DIST').exclude(type='')
        return render(request, 'distve.html', {'acc': acc, 'whom': whom})
    else:
        return redirect('dashboard')


@login_required
def addunit(request):
    form = UnitForm()
    userId = request.user.id
    who = Account.objects.get(id=userId)
    whom = who.name
    zone = Account.objects.filter(type='ZONE')
    cluster = Account.objects.filter(type='CLUSTER')
    if who.type == 'DIST':
        if request.method == 'POST':
            form = UnitForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.type = 'UNIT'
                obj.unit = obj.name
                password = obj.password
                obj.password = make_password(password)
                obj.save()
                messages.success(request, "Portal Added Successfully")
                return redirect('dashboard')
        return render(request, 'distunit.html', {'form': form, 'whom': whom, 'zone': zone, 'cluster': cluster})
    else:
        return redirect('dashboard')


@login_required
def addcluster(request):
    form = ClusterForm()
    userId = request.user.id
    who = Account.objects.get(id=userId)
    whom = who.name
    centre = Account.objects.filter(type='ZONE')
    if who.type == 'DIST':
        if request.method == 'POST':
            form = ClusterForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.type = 'CLUSTER'
                obj.cluster = obj.name
                obj.unit = 'NULL'
                password = obj.password
                obj.password = make_password(password)
                obj.save()
                messages.success(request, "Portal Added Successfully")
                return redirect('dashboard')
        return render(request, 'distcluster.html', {'form': form, 'whom': whom, 'centre': centre})
    else:
        return redirect('dashboard')


@login_required
def addzone(request):
    form = ZoneForm()
    userId = request.user.id
    who = Account.objects.get(id=userId)
    whom = who.name
    if who.type == 'DIST':
        if request.method == 'POST':
            form = ZoneForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.type = 'ZONE'
                obj.zone = obj.name
                obj.cluster = 'NULL'
                obj.unit = 'NULL'
                password = obj.password
                obj.password = make_password(password)
                obj.save()
                messages.success(request, "Portal Added Successfully")
                return redirect('dashboard')
        return render(request, 'distzone.html', {'form': form, 'whom': whom})
    else:
        return redirect('dashboard')


@login_required
def addcentre(request):
    form = CentreForm()
    userId = request.user.id
    who = Account.objects.get(id=userId)
    whom = who.name
    if who.type == 'DIST':
        if request.method == 'POST':
            form = CentreForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.type = 'CENTRE'
                obj.zone = 'NULL'
                obj.cluster = 'NULL'
                obj.unit = 'NULL'
                print("entered........!")
                password = obj.password
                obj.password = make_password(password)
                obj.save()
                messages.success(request, "Portal Added Successfully")
                return redirect('dashboard')
        return render(request, 'distcentre.html', {'form': form, 'whom': whom})
    else:
        return redirect('dashboard')


@login_required
def addmedshop(request):
    form = CentreForm()
    userId = request.user.id
    who = Account.objects.get(id=userId)
    whom = who.name
    if who.type == 'DIST':
        if request.method == 'POST':
            form = CentreForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.type = 'MEDSHOP'
                obj.zone = 'NULL'
                obj.cluster = 'NULL'
                obj.unit = 'NULL'
                password = obj.password
                obj.password = make_password(password)
                obj.save()
                messages.success(request, "Portal Added Successfully")
                return redirect('dashboard')
        return render(request, 'distmedshop.html', {'form': form, 'whom': whom})
    else:
        return redirect('dashboard')


@login_required
def medapprove(request, data_id):
    form = MedicineApproveForm()
    obj = medicine.objects.get(id=data_id)
    medshop = Account.objects.filter(type='MEDSHOP')
    userId = request.user.id
    who = Account.objects.get(id=userId)
    if who.type == 'DIST':
        if request.method == 'POST':
            form = MedicineApproveForm(request.POST)
            if form.is_valid():
                frm = form.save(commit=False)
                obj = medicine.objects.get(id=data_id)
                obj.dist_approve = 'APPROVED'
                obj.lastdat = frm.lastdat
                obj.medshop = frm.medshop
                if(frm.medrem=='5'):
                    obj.medrem = 2;
                else:    
                    obj.medrem = frm.medrem
                obj.dateofapp = datetime.datetime.now().replace(microsecond=0)
                obj.dist_approve_by = who.name
                otp_list = couponMaker(obj.medrem)
                obj.otp1 = otp_list[0]
                obj.otp2 = otp_list[1]
                obj.otp3 = otp_list[2]
                obj.otp4 = otp_list[3]
                obj.save()
                unitis = Account.objects.get(unit=obj.unit, cluster=obj.cluster, zone=obj.zone)
                message2 = 'Your Application ' + obj.mdcnumber + ' For Medicine is Approved. Coupon Codes:  ' + obj.otp1 + ', ' + obj.otp2 + ', ' + obj.otp3 + ' & ' + obj.otp4 + ' Last Date: ' + str(
                    obj.lastdat) + ' Medical Shop: ' + obj.medshop + '.%0A%0ASKSSF KANNUR'
                a = SmsSent(message2, unitis.phone, peid='1201161554659928564', teid='1207162954064793768')
                messages.success(request, "Medicine Approved Successfully")
                return redirect('dashboard')
        return render(request, 'distmedallocate.html', {'obj': obj, 'form': form, 'centre': medshop})
    else:
        return redirect('dashboard')


@login_required
def medrej(request, data_id):
    userId = request.user.id
    who = Account.objects.get(id=userId)
    if who.type == 'DIST':
        if request.method == 'POST':
            obj = medicine.objects.get(id=data_id)
            obj.dist_approve = 'REJECTED'
            obj.save()
            messages.success(request, "Medicine Rejected Successfully")
            return redirect('dashboard')
    else:
        return redirect('dashboard')


@login_required
def allocate(request, data_id):
    form = ApproveForm()
    obj = patient.objects.get(id=data_id)
    centre = Account.objects.filter(type='CENTRE')
    userId = request.user.id
    who = Account.objects.get(id=userId)
    if who.type == 'DIST':
        if request.method == 'POST':
            form = ApproveForm(request.POST)
            if form.is_valid():
                frm = form.save(commit=False)
                obj.dist_approve = 'APPROVED'
                obj.dist_time = datetime.datetime.now().replace(microsecond=0)
                frm.dylnumber = obj.dylnumber
                frm.phone = obj.phone
                frm.name = obj.name
                frm.age = obj.age
                frm.dylrem = frm.dylcount
                frm.address = obj.address
                otpcheck = 0
                while (otpcheck == 0):
                    otpcheck = get_random_string(length=5, allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
                    if approved.objects.filter(otp=otpcheck).exists():
                        otpcheck = 0
                frm.otp = otpcheck
                obj.centre = frm.centre
                frm.save()
                obj.save()
                message2 = 'Hi, ' + obj.name + ' Your Application for Dialysis is Approved by SKSSF KANNUR District. Your Coupon Code is:  ' + frm.otp + ' Your Hospital is ' + obj.centre + '.%0A%0ASKSSF KANNUR'
                a = SmsSent(message2, obj.phone, peid='1201161554659928564', teid='1207162954058282374')
                messages.success(request, "Dialysis Allotted Successfully")
                return redirect('dashboard')
        return render(request, 'distallocate.html', {'obj': obj, 'form': form, 'centre': centre})
    else:
        return redirect('dashboard')


@login_required()
def dylpatrep(request, data_id):
    userId = request.user.id
    who = Account.objects.get(id=userId)
    if who.type == 'DIST':
        dylpat = approved.objects.get(id=data_id)
        dylno = dylpat.dylnumber
        dyldone = centre.objects.filter(dylnumber=dylno).count()
        pendcount = int(dylpat.dylrem) - dyldone
        return render(request, 'distdylrep.html', {'centrename': dylno, 'done': dyldone, 'pend': pendcount})
    else:
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
