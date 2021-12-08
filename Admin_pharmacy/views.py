from django.shortcuts import render,redirect,HttpResponse
from pharmacy.models import pha_product,pharmacy_prod_order,pharmacy
from .models import  pharmacy_admin_record,supplier,category,Purchase,setting
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth import authenticate,login,logout


# Create your views here.



def index(request):
    list=[]
    docs=pharmacy.objects.get(id=request.user.pharmacy.id)
    product=pha_product.objects.filter(doc=docs)
    supp=supplier.objects.filter(user=docs)
    user=pharmacy_prod_order.objects.filter(pharmacys=docs)
    for i in user:
        if [i.username,i.phone,i.address] not in list:
            list.append([i.username,i.phone,i.address])

    return render(request,'home.html',{'product':list,'date':date.today(),'supp':len(supp),'prod':len(product)})
def categories(request):
    product=category.objects.all()
    # product = pharmacy.objects.filter(user=request.user.userType.id)
    if request.method == 'POST':  # for edit
        if request.POST.get('catid') is not None:
            name = request.POST['catname']
            products = category.objects.get(id=request.POST['catid'])
            products.cate = name
            products.save()
        elif request.POST.get('catename') is not None:#for add
            name = request.POST['catename']
            cate=category.objects.values('cate')
            data={data['cate'].lower() for data in cate}
            if name.lower() not in data:
                cat=category(cate=name)
                cat.save()
            else:
                messages.warning(request,'category is already in list')

    prod = request.GET.get('catids')#for delete
    products = category.objects.filter(id=prod)
    products.delete()

    return render(request,'categories.html',{'product':product})
def sales(request):
    pharmcy=pharmacy.objects.get(id=request.user.pharmacy.id)
    product = pharmacy_prod_order.objects.filter(pharmacys=pharmcy)

    prod = request.GET.get('product')  # for delete
    pro = pharmacy_prod_order.objects.filter(id=prod)
    pro.delete()

    ids = request.GET.get('productid')         #for edit
    pro = pharmacy_prod_order.objects.filter(id=ids)
    invoice_no=request.GET.get('invoice')
    if len(pro)>0:
        os=pro[0]
        os.invoice=invoice_no
        os.save()
    return render(request,'sales.html',{'product':product})
def transaction(request):
    pharmcy=pharmacy.objects.get(id=request.user.pharmacy.id)
    product = pharmacy_prod_order.objects.filter(pharmacys=pharmcy)
    ids = request.GET.get('orderid')  # for delete
    order = pharmacy_prod_order.objects.filter(id=ids)
    print(order, 'ppp')
    if len(order) > 0:
        ob = order[0]
        ob.delete()

    return render(request,'transactions-list.html',{'product':product})
def profile(request):
    ids = request.GET.get('id')
    pro=User.objects.get(id=request.user.id)
    profile=pharmacy_admin_record.objects.filter(user=pro)
    id = request.GET.get('adminid') #admin edit
    name = request.GET.get('name')
    about = request.GET.get('about')
    img = request.GET.get('img')
    profs=pharmacy_admin_record.objects.filter(id=id)

    if len(profs)>0:
        prof=profs[0]
        prof.about=about
        prof.name=name
        prof.img=img
        prof.save()
    # id = request.GET.get('id1')#for pwd change
    # old = request.GET.get('oldpwd')
    # new = request.GET.get('newpwd')
    # print(id,old,new,';;;;')
    if request.method=='POST': #for personal edit
        # id1 = request.POST.get('profileid')
        # if id1 is not None:
            id1 = request.POST['profileid']
            print(id1,'111')
            fname = request.POST['fname']
            lname = request.POST['lname']
            add = request.POST['address']
            city = request.POST['city']
            email = request.POST['email']
            state = request.POST['state']
            dob = request.POST['dob']
            mobile = request.POST['mobile']
            zip = request.POST['zipcode']
            country = request.POST['country']
            user=User.objects.get(id=request.user.id)
            user.firstname=fname
            user.lastname=lname
            user.save()
            print(user,'ppppppp')
            profiles = pharmacy_admin_record.objects.get(id=id1)
            profiles.address=add
            profiles.city=city
            profiles.state=state
            profiles.country=country
            profiles.dob=dob
            profiles.mobile = mobile
            profiles.email=email
            profiles.zipcode=zip
            profiles.save()
        # elif ids  is not None: # for pwd change
        #     print(request.POST['id1'])
        #     old = request.POST['oldpwd']
        #     new = request.POST['newpwd']
        #     user = User.objects.get(id=request.user.id)
        #     mail=user.email
        #     check=user.check_password(old)
        #     print(old,new,user,mail,check,'///////')
        #     if check==True:
        #         user.set_password(new)
        #         user.save()
        #         user=User.objects.get(email=mail)
        #         login(request,user)
        #         messages.error(request, "password updated")
        #     else:
        #         print('no match')
        #         messages.error(request, "incorrect old password")




    return render(request,'profile.html',{'profile':profile})
def settings(request):
    if request.method=='POST':
        webname=request.POST['webname']
        weblogo=request.POST['weblogo']
        favicon=request.POST['favicon']
        sett=pharmacy.objects.get(id=request.user.pharmacy.id)
        setts=setting.objects.filter(pharmacy=sett)
        if len(setts)>0:
            prod=setts[0]
            prod.pharmacy=sett
            prod.weblogo=weblogo
            prod.webname=webname
            prod.favicon=favicon
            prod.save()
        else:
            prods=setting(webname=webname,weblogo=weblogo,favican=favicon,pharmacy=sett)
            prods.save()
    return render(request,'settings.html')
def products(request):
    # phar=request.GET.get('phar_id')
    li=pharmacy.objects.get(id=request.user.pharmacy.id)
    products = pha_product.objects.filter(doc=li)
    print(products,'dd',li,';;')
    products1 = pha_product.objects.filter(id=request.GET.get('prod'))
    products1.delete()
    if request.method=='POST': # for edit
            pro=request.POST['phar_ids']
            name = request.POST['prodname']
            price = request.POST['price']
            dis = request.POST['discount']
            product1 = pha_product.objects.get(id=pro)
            # if len(products)>0:
            #     prod=products[0]
            product1.price=price
            product1.name=name
            product1.discount = dis
            product1.save()
            print(products,'//')
    return render(request,'products.html',{'product':products,'today':date.today()})
def add_product(request):
    cates=category.objects.all()
    phars = request.GET.get('phar_id')
    product2 = pharmacy.objects.get(id=request.user.pharmacy.id)
    # for i in product2:
    if request.method=='POST' :
        name=request.POST['prod_name']
        cate = request.POST['category']
        Price = request.POST['Price']
        quantity = request.POST['quantity']
        date = request.POST['ex_date']
        about = request.POST['about']
        images = request.FILES['img']

        prod_name = pha_product.objects.values('name').filter(doc=product2)
        list = {data['name'].lower() for data in prod_name}
        print(list,prod_name,'lil')
        if name.lower() not in list:
            product=pha_product(doc=product2,name=name,img=images,about=about,
                                price=Price,categorie=cate,quntity=quantity,expiry_date= date )
            product.save()

    messages.success(request, " Product Added Successfully")
        # print(product, 'pppp///')
    return render(request,'add-product.html',{'cates':cates})
def outstock(request):
    li = pharmacy.objects.filter(id=request.user.pharmacy.id)
    # phars = request.GET.get('phar')
    product2 = pharmacy.objects.get(id=request.user.pharmacy.id)
    products = pha_product.objects.filter(id=request.GET.get('prod') , doc=product2)#for delete
    products.delete()

    if request.method == 'POST':  # for edit
        phars = request.POST['phar_ids']
        name = request.POST['gen_name']
        qunt = request.POST['quntity']
        products = pha_product.objects.filter(id=phars)
        if len(products) > 0:
            prod = products[0]
            prod.quntity = qunt
            prod.genatic_name = name
            prod.save()

    return render(request,'outstock.html',{'list':li})
def purchase(request):
    pharmcy=pharmacy.objects.get(id=request.user.pharmacy.id)
    product = Purchase.objects.filter(pharmacys=pharmcy)
    supp=supplier.objects.filter(user=pharmcy)
    sup=request.GET.get('suppid')
    product1 = Purchase.objects.filter(id=sup)
    product1.delete()

    if request.method=='POST':
        supp1=request.POST['prod']
        suppl=request.POST['supp']
        prods = Purchase.objects.filter(id=supp1)
        supple=supplier.objects.get(name=suppl)
        if len(prods)>0:
            prod=prods[0]
            prod.supplir=supple
            prod.save()
    return render(request,'purchase.html',{'product':product,'supp':supp})
def add_purchase(request):
    pharmcy=pharmacy.objects.get(id=request.user.pharmacy.id)
    if request.method=='POST':
        medname = request.POST['med_name']
        qun = request.POST['qunt']
        price = request.POST['price']
        img = request.FILES['img']
        cate = request.POST['cate']
        exdate = request.POST['exdate']

        product = Purchase.objects.values('med_name')
        print('//',product)
        data = {data['med_name'].lower() for data in product}
        print('[[',data)
        if medname.lower() not in data:
            prod=Purchase(pharmacys=pharmcy,med_name=medname,price=price,quntity=qun,img=img,category=cate,ex_date=exdate)
            prod.save()
            print(prod,'..///')
    return render(request,'add-purchase.html')
def order(request):
    pharmcy=pharmacy.objects.get(id=request.user.pharmacy.id)
    product = pharmacy_prod_order.objects.filter(pharmacys=pharmcy)
    sup = request.GET.get('suppid')
    product1 = pharmacy_prod_order.objects.filter(id=sup,pharmacys=pharmcy)
    product1.delete()

    return render(request,'order.html',{'product':product})
def expired(request):
    cont= date.today()
    li=pharmacy.objects.filter(id=request.user.pharmacy.id)

    prod = pha_product.objects.filter(id=request.GET.get('ex_ids'))  # for delete
    prod.delete()

    if request.method=='POST':
            ids=request.POST['exid']
            exp = request.POST['expiry']
            gen = request.POST['gentic']
            prod=pha_product.objects.filter(id=ids)
            if len(prod)>0:
                prods=prod[0]
                prods.expiry_date=exp
                prods.genatic_name=gen
                prods.save()
    return render(request,'expired.html',{'li':li,'date':cont})
def suppliers(request):

    prods=pharmacy.objects.get(id=request.user.pharmacy.id)
    supply = supplier.objects.filter(user=prods)
    prod=pha_product.objects.filter(doc=request.user.pharmacy.id)# editing  options
    supplierid = request.GET.get('suppid')#for delete
    supp=supplier.objects.filter(id=supplierid)
    supp.delete()
    if request.method=='POST':#for edit
        supp = request.POST['supply']
        com = request.POST['company']
        names = request.POST['prod_name']
        supplier1=supplier.objects.filter(id=supp)
        product=pha_product.objects.get(name=names)
        print(supp,com,names,supplier1,product,product.name)
        if len(supplier1)>0:
            pro=supplier1[0]
            pro.company=com
            pro.product=product
            pro.save()
            print(pro,'[]]]]')
    return render(request,'supplier.html',{'supply':supply,'prod':prod})
def add_supplier(request):
    pharmcy=pharmacy.objects.get(id=request.user.pharmacy.id)
    if request.method=='POST':
        img = request.FILES['img[]']
        add = request.POST['address']
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        company = request.POST['company']


        prod_name = supplier.objects.values('email').filter(user=pharmcy)
        list = {data['email'].lower() for data in prod_name}
        if email.lower() not in list:
            supp=supplier(user=pharmcy,name=name,img=img,email=email,mobile=mobile,company=company,address=add)
            supp.save()
            return redirect('supplier')
    return render(request,'add-supplier.html')
def invoice_report(request):
    pharmcy=pharmacy.objects.get(id=request.user.pharmacy.id)

    product = pharmacy_prod_order.objects.filter(pharmacys=pharmcy)
    ids = request.GET.get('oderids') #for delete
    order = pharmacy_prod_order.objects.filter(id=ids)
    order.delete()
    order_id=request.GET.get('orderid')  # for edit details
    order=pharmacy_prod_order.objects.filter(id=order_id)
    invoice = request.GET.get('In_no')
    status = request.GET.get('status')
    if len(order)>0:
        ob=order[0]
        ob.invoice=invoice
        ob.payment_status=status
        ob.save()
    return render(request,'invoice-report.html',{'product':product})
def invoice_views(request):
    invoices=request.GET.get('invoice_no')
    all=0
    subtotal=0
    pharmcy=pharmacy.objects.get(id=request.user.pharmacy.id)
    prod=pharmacy_prod_order.objects.filter(id=invoices,pharmacys=pharmcy)
    for i in prod:
        all = (i.total- (i.total * (i.product_id.discount / 100)))
        subtotal=i.quntitys*i.price
    return render(request,'invoice-views.html',{'prod':prod,'all':int(all),'subtotal':subtotal})
