
# Create your views here.
from django.shortcuts import render,redirect
from .models import patient_record,patient_dashB,checkout,favourite,appoinmentlist,prescriptions,billings,medical_records
from pharmacy.models import pharmacy_prod_order
from doctors.models import Dr,for_bookings,book_times,book_timed,mypatient,reView,userType
from django.contrib import messages
from django.contrib.auth.models import User

#for login
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login,logout

# Create your views here.
month = {
      'Jan': "01",
      'Feb': "02",
      'Mar': "03",
      'Apr': "04",
      'May': "05",
      'Jun': "06",
      'Jul': "07",
      'Aug': "08",
      'Sep': "09",
      'Oct': "10",
      'Nov': "11",
      'Dec': "12"
    }

def booking(request):
    bid = request.GET.get('@//@/')
    profile = Dr.objects.get(id=bid)
    drs=for_bookings.objects.filter(name=profile)
    li=[]
    for i in drs:
        book=book_times.objects.filter(dr=i)
        li.append(book)
    res={'title': profile,'books':li}

    return render(request,'patient/booking.html',res)
def checkouts(request):
    # if request.user.is_authenticated:
        bid = request.GET.get('@//@/')
        profile = Dr.objects.get(id=bid)
        fess = profile.fees_starting
        total = fess + 10 + 50
        ids=request.user.patient_record.id
        patient=patient_record.objects.get(id=ids)
        date = request.GET.get('date')
        time1 = request.GET.get('time1')
        # book = for_bookings.objects.get(id=date)
        t = book_timed.objects.get(id=time1)
        date=request.GET.get('date')
        time1 = request.GET.get('time1')
        book = for_bookings.objects.get(id=date)
        t=book_timed.objects.filter(id=time1)
        res = {'title': profile, 'total': total,'date':book.date,'t':t}

        return render(request,'patient/checkout.html',res)
def booking_success(request):
    bid = request.GET.get('Did')
    bids = request.GET.get('pid')
    time1 = request.GET.get('time1')
    patient = patient_record.objects.get(id=bids)
    profile = Dr.objects.get(id=bid)
    t = book_timed.objects.get(id=time1)
    res={}
    if request.method=='POST':
        phone = request.POST['phone']
        date = request.POST['date']
        t1 = t.time1
        t2 = t.time2
        card_name = request.POST['cardname']
        card_no = request.POST['cardno']
        exmonth = request.POST['exmonth']
        exyear = request.POST['exyear']
        cvv = request.POST['cvv']
        amount = request.POST['amount']
        print(date,'ll')
        date = (date[8:] + "-" + str(month.get(date[:3])) + "-" + date[5:7]).replace(' ', '')
        alredy_data=checkout.objects.filter(dr_name=profile, patient=patient,date=date, time1=t1, time2=t2)
        if len(alredy_data)>0:
            messages.warning(request,'Appointment is already book at this timing.')
        else:
            check = checkout(phone=phone, date=date, time1=t1, time2=t2, card_name=card_name, card_no=card_no,
                         cvv=cvv, exp_year=exyear, exp_month=exmonth, amount=amount, email=request.user.email,
                         dr_name=profile, patient=patient)
            check.save()
            appoinmentlists = appoinmentlist(date=date, time1=t1, time2=t2, card_name=card_name, card_no=card_no,
                                             cvv=cvv, exp_year=exyear, exp_month=exmonth, amount=amount,
                                             doctor=profile, patient=patient)
            appoinmentlists.save()
            messages.success(request, "Booking confirm successfully.")
            checks = appoinmentlist.objects.filter(patient=patient,doctor=profile,date=date, time1=t1, time2=t2)
            res={'user':checks}
    return render(request,'patient/booking-success.html',res)
def invoice_view(request):
    bid = request.GET.get('Pid')
    bids = request.GET.get('Did')
    bi = request.GET.get('Oid')
    Bid = request.GET.get('Bid')
    dr=Dr.objects.get(id=bids)
    patient=patient_record.objects.get(id=bid)
    checks = appoinmentlist.objects.filter(doctor=dr,patient=patient,id=bi)
    billing=billings.objects.filter(doctor=dr,patient=patient,id=Bid)
    print(billing,'iiiiiiiiiiiiii')
    res = {'user': checks,'bills':billing}

    return render(request,'patient/invoice-view.html',res)
def order_list(request):
    list=pharmacy_prod_order.objects.filter(username=request.user.username)
    print(list,'lolol')
    ids=request.GET.get('id')
    if ids is not None:
        order=pharmacy_prod_order.objects.get(id=ids)
        order.delete()
        print(ids,order)
    return render(request,'patient/order-list.html',{'list':list})
def add_medical_record(request):
    ids=patient_record.objects.get(id=request.user.patient_record.id)
    record= medical_records.objects.filter(patient=ids)
    return render(request,'patient/add_medical_record.html', {'record': record})
def profile_setting(request):
        userids = request.GET.get('profile')
        if request.method == "POST":
            fname = request.POST['fname']
            lname = request.POST['lname']
            user = User.objects.get(id=request.user.id)
            user.first_name = fname
            user.last_name = lname
            user.save()
            img = request.POST['img']
            # email = request.POST['email']
            phone = request.POST['phone']
            bloodgrp=request.POST['bloodgrp']
            DOB=request.POST['DOB']
            age = request.POST['age']
            gender = request.POST['gender']
            # address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            country= request.POST['country']
            zip = request.POST['zip']

            patient = patient_record.objects.filter(id=request.user.patient_record.id)
            if len(patient) > 0:
                ob = patient[0]
                ob.name = request.user.username
                ob.img = img
                ob.email = request.user.email
                ob.mobile=phone
                ob.address =city
                ob.DOB = DOB
                ob.Blood_group =bloodgrp
                ob.age=age
                ob.gender = gender
                ob.save()
                messages.success(request, 'profile updated ')

        return render(request,'patient/profile-settings.html')
def patient_register(request):

    userlist=patient_record.objects.values('email')
    userlis={data['email'].lower() for data in userlist}
    if request.method == "POST":
            names = request.POST['names']
            emails = request.POST['emails']
            passwords = request.POST['passwords']
            confirm = request.POST['confirm']
            if emails.lower() not in userlis:
                user = User.objects.create_user(username=names, email=emails, password=passwords)
                user.save()
                user1 = patient_record(patient=user, name=names,age=0, email=emails,DOB='1998-4-2',mobile=0)
                user1.save()
                typeuser = userType(user=user, type='1')
                typeuser.save()
                if user is None:
                    messages.error(request, "invalid user")
                else:
                    messages.success(request, "Your account has been successfully created")
                return redirect('home')
            else:
                messages.error(request, "This Email is already register.")

    return render(request,'patient/patient-register.html')
def change_password(request):
        if request.method == "POST":
            old = request.POST['oldpwd']
            new = request.POST['newpwd']
            # confirm = request.POST['cnfpwd']
            user = User.objects.get(id=request.user.id)
            mail=user.email
            check=user.check_password(old)
            if check==True:
                user.set_password(new)
                user.save()
                user=User.objects.get(email=mail)
                login(request,user)
                messages.error(request, "password updated")
            else:
                print('no match')
                messages.error(request, "incorrect old password")
            return redirect('change_password')
        return render(request,'patient/change-password.html')
def patient_profile(request):
    pat = request.GET.get('profile')
    list = patient_record.objects.filter(id=pat)
    patients = patient_record.objects.get(id=pat)
    prec=prescriptions.objects.filter(patient=patients)
    bill=billings.objects.filter(patient=patients)
    medical=medical_records.objects.filter(patient=patients)
    app=appoinmentlist.objects.filter(patient=patients).last()
    # apps=app.objects.last()
    # print(app,'======',app.doctor.name)

    if request.method=='POST':
        if request.POST.get('Did') is not None:
            date=request.POST['date']
            file = request.POST['file']
            desc = request.POST['dese']
            Did = request.POST['Did']
            dr=Dr.objects.get(id=Did)
            print(date,file,desc,'ffff',Did)
            med=medical_records(doctor=dr,date=date,attachment=file,desc=desc,patient=patients)
            med.save()
            print(med,'mmm')
        elif request.POST.get('Dids') is not None:
            date = request.POST['date']
            Did = request.POST['Dids']
            dr=Dr.objects.get(id=Did)
            print(date,Did,dr,'//')
            pres=prescriptions(doctor=dr,date=date,patient=patients)
            pres.save()
        elif request.POST.get('Did1') is not None:
            date = request.POST['date']
            amount = request.POST['amount']
            Did = request.POST['Did1']
            dr=Dr.objects.get(id=Did)
            print(date,Did,dr,'//')
            pres=billings(doctor=dr,paid_on_date=date,amount=amount,patient=patients,invoice_no=0)
            pres.save()
    res={'list':list,'prec':prec,'bill':bill,'medical':medical,'last':app}
    return render(request,'patient/patient-profile.html',res)
def favourites(request):
    fav1 = request.GET.get('pa')
    pa = patient_record.objects.get(patient=request.user.id)
    favr = favourite.objects.filter(pa_name=pa)
    res = {'fav': favr}
    return render(request, 'patient/favourites.html',res)
def favt(request):
    fav = request.GET.get('dr')
    fav1 = request.GET.get('pa')
    dr = Dr.objects.get(id=fav)
    pa = patient_record.objects.get(patient=fav1)
    favv=favourite.objects.filter(dr_name=dr, pa_name=pa)
    if len(favv)>0:
        ob=favv[0]
        ob.dr_name=dr
        ob.pa_name=pa
        ob.save()
    else:
        favs = favourite(dr_name=dr, pa_name=pa)
        favs.save()
    return redirect('favourites')
def patient_dashboard(request):
    pa=request.GET.get('Pid')
    patients =patient_record.objects.get(id=pa)
    list = checkout.objects.filter(patient=patients)
    prec = prescriptions.objects.filter(patient=patients)
    bill = billings.objects.filter(patient=patients)
    medical = medical_records.objects.filter(patient=patients)
    print(prec, '[[[[[[[')
    return render(request, 'patient/patient-dashboard.html',{'list':list,'prec':prec,'bill':bill,'medical':medical})
def Search(request):
    doctor=Dr.objects.all()
    gender = Dr.objects.values('gender')
    gender = {datas['gender'] for datas in gender}
    li = []
    list = []

    pa_names=patient_record.objects.get(id=request.user.patient_record.id)# for favourite checked
    favt=favourite.objects.values('dr_name').filter(pa_name=pa_names)
    fav=[i['dr_name'] for i in favt]

    speciality = Dr.objects.values('specialization')
    speciality = {data['specialization'] for data in speciality}
    if request.method != 'POST' :
        li.append(Dr.objects.all())
    else:
        doctor_list = request.POST.getlist("data")
        doctor_lists = request.POST.getlist("datas")
        data = ''
        if (len(doctor_list) > 0) and (len(doctor_lists)>0):
            for data1 in doctor_list:
                data = data + data1 + " "
                dr=Dr.objects.filter(specialization=data1)
                for data2 in doctor_lists:
                    data = data + data2 + " "
                    dr = Dr.objects.filter(gender=data2,specialization=data1)
                li.append(dr)
                for i in dr:
                    x = i.specialization
                    y=i.gender
                list.append(x)
                list.append(y)
        else:
            for data3 in doctor_list:
                data = data + data3 + " "
                dr = Dr.objects.filter(specialization=data3)
                li.append(dr)
                for i in dr:
                    x=i.specialization
                list.append(x)
            else:
                  for data2 in doctor_lists:
                    data = data + data2 + " "
                    dr = Dr.objects.filter(gender=data2)
                    li.append(dr)
                    for i in dr:
                        x = i.gender
                    list.append(x)
    count = 0
    for i in li:
        for j in i:
          count += 1
    res={'title':doctor,'gender':gender,'speciality':speciality,'li':li,'count':count,'list':list,'favt':fav}
    return render(request, 'patient/search.html',res)







