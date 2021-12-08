from django.shortcuts import render,redirect
from .models import Dr,Ov_view,Exp_erince, Educat_ion,userType,Buss_Ho,Loca_tions,servies_add,\
    specifications_add,Specific_ation,Awards,mypatient,reView,Hour_S,servi_ses,book_times,for_bookings
from patient.models import checkout,patient_record,patient_dashB,favourite,appoinmentlist,prescriptions,medical_records,billings
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import date
#for login
from django.contrib.auth import authenticate,login,logout

def Doctor_profile(request,id):
         # bid= request.GET.get('@//@/')
         profile=Dr.objects.get(id=id)
         patient = patient_record.objects.values('name')
         patients = {data['name'] for data in patient}

         # pa_names = patient_record.objects.get(id=request.user.patient_record.id)  # for favourite checked
         # favt = favourite.objects.values('dr_name').filter(pa_name=pa_names)
         # fav = [i['dr_name'] for i in favt]

         if request.method == "POST":
            name = request.POST['name']
            review = request.POST['review']
            rating = request.POST['rating']
            patient1 = patient_record.objects.get(name=name)
            print(rating,'ratttttttt',name,review,patient1)
            if name in patients:
                var = reView(patient=patient1,name=name, review=review,dics=profile,YES=0,NO=0,rating=rating)
                var.save()
            else:
                 messages.success(request, "Your are not patient")
         review = reView.objects.filter(dics=profile)
         res={'title':profile,'review':review}
         return render(request,'doctor/doctor-profile.html',res)
def Doctor_register(request):
    userlist=Dr.objects.values('email')
    userlis={data['email'].lower() for data in userlist}
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm=request.POST['confirm']
        if email.lower()  not in userlis:
            user =User.objects.create_user(username=name, email=email, password=password)
            user.save()
            name1 = request.POST['name']
            email1 = request.POST['email']
            user1 = Dr(user=user, name=name1, email=email1,fees_starting=0,fees_end=0 )
            user1.save()
            typeuser = userType(user=user, type='2')
            typeuser.save()
            if user is None:
                messages.error(request, "invalid user")
            else:
                messages.success(request, "Your account has been successfully created")
            return redirect('home')
        else:
            messages.error(request, "This Email is already register.")

    return render(request,'doctor/doctor-register.html')
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
                messages.error(request, "incorrect old password")
            return redirect('change_password')
        return render(request,'patient/change-password.html')
def dlogin(request):
    if request.method=='POST':
         loginemail = request.POST['email']
         username = User.objects.get(email=loginemail).username
         pass1 = request.POST['password']
         user= authenticate(username=username,password=pass1)
         if user is not None:
            login(request,user)
            if not request.user.is_authenticated:
               messages.success(request, 'user none')
               return redirect('dlogin')
            else:
                messages.success(request,F'{username} you are successfully logged In')
                return redirect('home')
         messages.error(request, 'Invalid email or password')
         return redirect('dlogin')
    return render(request,'login.html')
def dlogout(request):
    logout(request)
    messages.success(request,'you are successfully logged Out')
    return redirect('home')
def doctor_dashboard(request):
    dr = Dr.objects.get(id=request.user.Dr.id)
    list= checkout.objects.filter(dr_name=dr)
    totalapp=len(list)

    doctors=Dr.objects.get(id=request.user.Dr.id)
    p_list=mypatient.objects.filter(Dr_names=doctors)
    current_date=date.today()
    return render(request,'doctor/doctor-dashboard.html',{'list':list,'now':current_date,'length':totalapp,'pcount':len(p_list)})
def doctor_profile_setting(request):
    if request.user.is_authenticated:
        print(specifications_add.objects.all(),'//////////////')
        userids=request.GET.get('profile')
        # doctor1 = User.objects.get(id=userids)
        print(userids,'uu')
        doctor=Dr.objects.filter(id=userids)

        profile = Dr.objects.get(id=userids)
        print(doctor,';;;;',userids,profile)
        if request.method == "POST":
                    fname = request.POST['fname']
                    lname = request.POST['lname']
                    user = User.objects.get(id=request.user.id)
                    user.first_name = fname
                    user.last_name = lname
                    user.save()
                    img = request.POST['img']
                    qulification = request.POST['qulification']
                    speciality = request.POST['speciality']
                    fees1 = request.POST['f1']
                    fees2= request.POST['f2']
                    city = request.POST['city']
                    gender = request.POST['gender']
                    if len(doctor)>0:
                        ob = doctor[0]
                        ob.user=user
                        ob.name = request.user.username
                        ob.email = request.user.email
                        ob.img = img
                        ob.qulification= qulification
                        ob.specialization=speciality
                        ob.address = city
                        ob.fees_starting=fees1
                        ob.fees_end = fees2
                        ob.gender=gender
                        ob.save()
                    # user = Dr(user=user,name= request.user.username,email=request.user.email,img=img,qulification=qulification,
                    #       specialization=speciality,address=city,fees_starting=fees1,fees_end=fees2)
                    # user.user.save()
                    # print('userrrrr',user)
                    # profile = Dr.objects.filter(id=userids)

                    about = request.POST['about']
                    user1 = Ov_view(doc=profile, about=about)
                    user1.save()

                    profile1 = Ov_view.objects.get(doc=user1)

                    # services = request.POST['services']
                    # ser=servies_add.objects.get(service=services)
                    # user1 = servi_ses(dr=profile1,servics=ser)
                    # user1.save()

                    #
                    # if len(ser)>0:
                    #     ob=ser[0]
                    #     ob.service=services
                    #     # ob.save()
                    #     print(ob,ob.id,'ooo')
                    #     users1 = servi_ses(dr=profile1)
                    #     users1.servics.add(request.ob.service)
                    #     users1.save()
                    # else:
                    #     print('invalid servise')

                    # specialist = request.POST['specialist']
                    # spec=specifications_add.objects.get(specifications=specialist)
                    # user1 = Specific_ation(dr=profile1,specification=spec)
                    # user1.save()
                    # us = user1.specification.create(specifications=spec)
                    # print(user1,'//specc')

                    aw_name = request.POST['aw_name']
                    year = request.POST['year']
                    field = request.POST['field']
                    awrd=Awards.objects.filter(dr=profile1, aw_name=aw_name,aw_desc=field)
                    if len(awrd)>0:
                        aw=awrd[0]
                        aw.dr = profile1
                        aw.aw_name = aw_name
                        aw.aw_year = year
                        aw.aw_desc = field
                        aw.save()
                    else:
                        user1 = Awards(dr=profile1, aw_name=aw_name,aw_year=year,aw_desc=field)
                        user1.save()

                    institude = request.POST['institude']
                    YOC = request.POST['YOC']
                    YOA = request.POST['YOA']
                    degree = request.POST['degree']
                    edu=Educat_ion.objects.filter(dr=profile1,degree=degree)
                    if len(edu) > 0:
                        ed = edu[0]
                        ed.dr = profile1
                        ed.univercity = institude
                        ed.degree = degree
                        ed.YOP = YOC
                        ed.YOA = YOA
                        ed.save()
                    else:
                        user1 = Educat_ion(dr=profile1, univercity=institude,degree=degree,YOP=YOC,YOA=YOA)
                        user1.save()

                    hosp_name = request.POST['hosp_name']
                    yop = request.POST['yop']
                    yop1 = request.POST['yop1']
                    designation=request.POST['designation']
                    exp=Exp_erince.objects.filter(dr=profile1,exp_filled =hosp_name,experince=designation)
                    if len(exp)>0:
                        ex=exp[0]
                        ex.dr = profile1
                        ex.exp_filled = hosp_name
                        ex.YO_exp_start = yop
                        ex.YO_exp_till = yop1
                        ex.experince = designation
                        ex.save()
                    else:
                        user1 = Exp_erince(dr=profile1,exp_filled =hosp_name,YO_exp_start = yop,YO_exp_till = yop1,experince=designation)
                        user1.save()

                    name = request.POST['cli_name']
                    fee = request.POST['fees']
                    add = request.POST['clinic_add']
                    loc= Loca_tions.objects.filter(doc=profile,clinics_name=name)
                    if len(loc)>0:
                        locs=loc[0]
                        locs.doc = profile
                        locs.clinics_name = name
                        locs.clinic_add = add
                        locs.fees = fee
                        locs.save()
                    else:
                        user1 = Loca_tions(doc=profile,clinics_name=name, clinic_add=add,fees=fee)
                        user1.save()
            # add2 = request.POST['add2']
            # add3 = request.POST['add3']
            # city = request.POST['city']
            # state = request.POST['state']
            # country = request.POST['country']
            # postalcode = request.POST['postalcode']
            #
            # membership = request.POST['membership']
            # registration = request.POST['registration']
            # # res_year = request.POST['res_year']
                    messages.success(request, 'profile updated ')
    res={'spec':specifications_add.objects.all(),'serv':servies_add.objects.all()}
    return render(request,'doctor/doctor-profile-settings.html',res)
def reviews(request):
    dr=Dr.objects.get(id=request.user.Dr.id)
    rev=reView.objects.filter(dics=dr)

    return render(request,'doctor/reviews.html',{'review':rev})
def like(request):
    bid=request.GET.get('@//@/')
    next=request.GET.get('next')
    prod_list = reView.objects.filter(id=bid)
    # print(prod_list,'.////')
    if len(prod_list) > 0:
        ob = prod_list[0]
        if ob.YES >= 0:
            ob.YES+= 1
            ob.save()
    return redirect(next)
def dislike(request):
    bid=request.GET.get('@//@/')
    next = request.GET.get('next')
    prod_list = reView.objects.filter(id=bid)
    if len(prod_list) > 0:
        ob = prod_list[0]
        if ob.NO >= 0:
            ob.NO+= 1
            ob.save()
    return redirect(next)
def appointments(request):

    doctor=request.GET.get('doctor')
    dr=Dr.objects.get(id=doctor)
    appoin=checkout.objects.filter(dr_name=dr)
    res={'app':appoin}
    return render(request,'doctor/appointments.html',res)
def appo_delete(request):

    # app_id = request.GET.get('id')
    checkid=request.GET.get('id')
    next = request.GET.get('next')
    check=checkout.objects.get(id=checkid)
    check.delete()
    # appo=appoinmentlist.objects.get(id=checkid)
    print(check,'ppppppppp')

    return redirect(next)
def schedule(request):
    dr=Dr.objects.get(id=request.user.Dr.id)
    time=for_bookings.objects.filter(name=dr)
    day = for_bookings.objects.values('day')
    days = {datas['day'] for datas in day}
    x=request.GET.get('dayy')
    x1=book_times.objects.filter(id=x)

    time1 = request.GET.get('timeid')
    day = request.GET.get('dayid')
    p=book_times.objects.filter(times=time1,dr=day)
    for i in p:
        z=i.times.remove(time1)
    res={'time':time,'days':days,'x':x1}
    return render(request,'doctor/schedule-timings.html',res)
def invoices(request):
    doctor = request.GET.get('invoice')
    dr = Dr.objects.get(id=doctor)
    invoice = appoinmentlist.objects.filter(doctor=dr)
    if request.GET.get('Oid') is not None:
        oderid = request.GET.get('Oid')
        pat_id = request.GET.get('pid')
        pat=patient_record.objects.get(id=pat_id)
        check = appoinmentlist.objects.get(patient=pat,id=oderid)
        check.delete()
        print(check,'ckk')

    res = {'invoice': invoice}
    return render(request,'doctor/invoices.html',res)
def chat_doctor(request):
    dr = Dr.objects.get(id=request.user.Dr.id)
    chat = checkout.objects.filter(dr_name=dr)
    li=[]
    for i in chat:
        pat=patient_record.objects.get(id=i.patient.id)
        if pat not in li:

          li.append(pat)

    return render(request,'doctor/chat-doctor.html',{'list':li})
def checkup(request):
    patientid = request.GET.get('id')
    patients=patient_record.objects.filter(id=patientid)
    # timing=checkout.objects.filter(id=patientid)
    oid = request.GET.get('Oid')
    patents=patient_record.objects.get(id=patientid)
    tiing=checkout.objects.filter(id=oid,patient=patents)

    tiings=appoinmentlist.objects.filter(id=oid,patient=patents)
    res = {'patient': patients,'time':tiing,'time1':tiings}

    return render(request,'doctor/checkup.html',res)
def my_patients(request):
    doctors=Dr.objects.get(id=request.user.Dr.id)
    patientlist=mypatient.objects.filter(Dr_names=doctors)
    print(patientlist,'llll')
    if len(patientlist) is 0:
        messages.success(request, 'No Patient Record')
    return render(request,'doctor/my-patients.html',{'list':patientlist})
def allpatient(request):
    dr_id=request.GET.get('doctor')
    pa_id = request.GET.get('pa_id')
    doctors=Dr.objects.get(id=dr_id)
    patients=patient_record.objects.get(id=pa_id)
    Oid = request.GET.get('Oid')
    # my_patients = mypatient.objects.filter(Dr_names=doctors, pa_names=patients)
    check = checkout.objects.filter(dr_name=doctors, patient=patients,id=Oid)
    patientid = request.GET.get('pa_id')
    patients = patient_record.objects.filter(id=request.GET.get('pa_id'))
    # timing = checkout.objects.filter(id=patientid)
    # oid = request.GET.get('Oid')
    # patents = patient_record.objects.get(id=patientid)
    # tiing = checkout.objects.filter(id=oid, patient=patents)
    #
    # tiings = appoinmentlist.objects.filter(id=oid, patient=patents)
    print(patients,'ppoo')
    patient1 = patient_record.objects.get(id=patientid)
    patientss = User.objects.get(username=patient1.name)
    age = request.POST.get('age')
    BG = request.POST.get('bgroup')
    gender = request.POST['gender']
    dob = request.POST.get('dob')
    if len(patients) > 0:
        ob = patients[0]
        ob.patient = patientss
        ob.age = age
        ob.gender = gender
        ob.Blood_group = BG
        ob.DOB = dob
        ob.save()
    else:
        patient = patient_record(patient=patientss, age=age, Blood_group=BG, DOB=dob,gender=gender)
        patient.save()
    BP = request.POST.get('BP')
    BP1 = request.POST.get('BP1')
    GL = request.POST.get('GL')
    GL1 = request.POST.get('GL1')
    BT = request.POST.get('BT')
    HR = request.POST.get('HR')
    pat = patient_record.objects.filter(id=request.GET.get('pa_id'))
    print(pat,'///')
    if len(pat) > 0:
        os = pat[0]
        os.patient_name = patient1
        os.heart_rate = HR
        os.BP_mg = BP
        os.BP_dl = BP1
        os.body_temp = BT
        os.Glucose_Level_up = GL
        os.Glucose_Level_to = GL1
        os.BMI_Status = 0
        os.Heart_Rate_Status = 0
        os.FBC_Status = 0
        os.Weight_Status = 0
        os.save()
    else:
        patient1 = patient_record.objects.get(id=pa_id)
        patients = patient_dashB(patient_name=patient1, heart_rate=HR, BP_mg=BP, BP_dl=BP1,
                                 body_temp=BT, Glucose_Level_up=GL, Glucose_Level_to=GL1,
                                 BMI_Status=0, Heart_Rate_Status=0, FBC_Status=0, Weight_Status=0)
        patients.save()
    messages.success(request, 'successfully detail updated')
    for data in check:
        pa_id=data.patient
        dr_id=data.dr_name
        my_patients = mypatient.objects.filter(Dr_names=dr_id, pa_names=pa_id)

        prec=prescriptions(patient=pa_id,date=data.date,doctor=dr_id)
        prec.save()
        bill=billings(patient=pa_id,doctor=dr_id,amount=data.amount,paid_on_date=data.date,invoice_no=0)
        bill.save()
        medical=medical_records(patient=pa_id,desc='',attachment='',date=data.date,doctor=dr_id)
        medical.save()

        if len(my_patients)>0:
            ob=my_patients[0]
            ob.Dr_names=dr_id
            ob.pa_names=pa_id
            ob.save()
        else:
            my_patienT = mypatient(Dr_names=dr_id, pa_names=pa_id)
            my_patienT.save()
        data.delete()
    return redirect('my_patient')


