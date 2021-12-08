import datetime
from django.shortcuts import render,redirect
from .models import pha_Oview,pha_product,pha_review,pharmacy,product_cart,pharmacy_prod_order
from Admin_pharmacy.models import pharmacy_admin_record
from doctors.models import userType
from django.contrib import messages
from django.contrib.auth.models import User
from patient.models import patient_record

# Create your views here.

def pharmacy_details(request):
    bid = request.GET.get('@//@/')
    pha= pharmacy.objects.all()
    medical = pharmacy.objects.get(id=bid)
    reviews = pha_review.objects.filter(dics=medical.id)

    patient = patient_record.objects.values('name')
    patients = {data['name'] for data in patient}
    if request.method == "POST":
        name = request.POST['title']
        review = request.POST['review']
        rating = request.POST['rating']
        if name in patients:
            var = pha_review(name=name, review=review,dics=medical,YES=0,NO=0,rating=rating)
            var.save()
        else:
            messages.success(request, "Your are not patient")

    res = {'title': medical}

    return render(request,'pharmacy/pharmacy-details.html',res)
def pharmacy_search(request):
    medical=pharmacy.objects.all()
    res={'title':medical}
    return render(request,'pharmacy/pharmacy-search.html',res)
def product_description(request):

    bdid = request.GET.get('@//@/')
    product1 = pha_product.objects.get(id=bdid)

    res={'title':product1}
    return render(request,'pharmacy/product-description.html',res)
def product_all(request):
    list=[]
    re={}
    total=0
    bdid=request.GET.get('@//@/')# for product description
    if bdid is None:
        # prod_list = pha_product.objects.all()
        list.append(pha_product.objects.all())
        categories1 = pha_product.objects.values('categorie')
        categories = {data['categorie'] for data in categories1}
        re.update({'cat': categories})
        if request.method == 'POST':
            cat_filter = request.POST.getlist('cat1')
            data=''
            list.clear()
            if len(cat_filter) > 0:
                for i in cat_filter:
                    data = data + i + " "
                    prod_list1 = pha_product.objects.filter(categorie=i)
                    list.append(prod_list1)
                    print(cat_filter, '///--', prod_list1)
        p=pha_product.objects.all().count()
        total+=p
    else:
        product=pharmacy.objects.get(id=bdid)
        prod_list = pha_product.objects.filter(doc=product)
        list.append(prod_list)
        categories1 = pha_product.objects.values('categorie').filter(doc=product)
        categories = {data['categorie'] for data in categories1}
        print(categories,'ccccccc')
        re.update({'cat':categories})
        if request.method=='POST':
            cat_filter = request.POST.getlist('cat1')
            data = ''
            list.clear()
            if len(cat_filter)>0:
                for i in cat_filter:
                    data = data + i + " "
                    prod_list1 = pha_product.objects.filter(doc=product,categorie=i)
                    list.append(prod_list1)
                    print(cat_filter,'///',prod_list1)
        p = pha_product.objects.filter(doc=product).count()
        total += p
    count = 0
    for i in list:
        for j in i:
            count += 1
    res = {'title':list,'cat':re,'count':count,'total':total}

    return render(request,'pharmacy/product-all.html',res)
def pharmacy_register(request):

    userlist=pharmacy.objects.values('email')
    userlis={data['email'] for data in userlist}
    if request.method == "POST":
            names = request.POST['name']
            emails = request.POST['email']
            passwords = request.POST['password']
            if emails not in userlis:
                user = User.objects.create_user(username=names, email=emails, password=passwords)
                user.save()
                usr = pharmacy_admin_record(user=user)
                usr.save()
                typeuser=userType(user=user,type='5')
                typeuser.save()
                pharma=pharmacy(email=emails,user=user,name=names,contact=0,opentime=datetime.datetime.now(),clostime=datetime.datetime.now())
                pharma.save()
                print(user,usr,'[[[[[[[[',typeuser,pharma)

                # print(typeuser,'yyyy')
                if user is None:
                    messages.error(request, "invalid user")
                else:
                    messages.success(request, "Your account has been successfully created")
                return redirect('home')
            else:
                messages.error(request, "This Email is already register.")

    return render(request,'pharmacy/pharmacy-register.html')
def medicine_cart(request):
    itemlist=product_cart.objects.filter(user_id=request.user.id)
    li=[]
    dic={}
    total=0
    print(itemlist,'\8\\')
    # ob=product_cart.objects.all()
    # ob.delete()
    # print(ob,'===')
    for data in itemlist:
        pharmacy_id=data.pharmacy_name
        prodct_id=data.product_id
        print(prodct_id,';;;;;;',data.id)
        products=pha_product.objects.get(id=prodct_id)
        allprice=products.price*data.quntity
        total+=allprice
        li.append([products,allprice,data.quntity])
        sub=total+25 #shippnig/tax
        all=(sub-(sub*(products.discount/100)))
        dic={'product':li,'total':total,'sub':sub,'alltotal':all,'dis':products.discount}
    return render(request,'pharmacy/cart.html',dic)
def add_to_cart(request):
    if request.user.is_authenticated:
        product_id = request.GET.get('@//@/')
        pharmacy_id = request.GET.get('next')
        product = pha_product.objects.get(doc=pharmacy_id,id=product_id)
        cartitem=product_cart.objects.filter(user_id=request.user.id,pharmacy_name=product.doc.name,product_id=product_id)
        if len(cartitem)>0:
            ob = cartitem[0]
            ob.quntity += 1
            ob.save()
        else:
            products=product_cart(user_id=request.user.id,Sku_no=product.doc.id,pharmacy_name=product.doc.name,quntity=1,product_id=product.id)
            products.save()
    print(product_cart.objects.all(),'[[[[[')
    return redirect('medicine_cart')
def minus(request):
    prodid = request.GET.get('quntity')
    docid = request.GET.get('next')
    itemlist = product_cart.objects.filter(user_id=request.user.id, product_id=prodid,pharmacy_name=docid)
    if len(itemlist) > 0:
        ob = itemlist[0]
        if ob.quntity != 0:
            ob.quntity -= 1
            ob.save()
        else:
            ob.delete()
    return redirect('medicine_cart')
def plus(request):
    prodid = request.GET.get('quntity')
    docid = request.GET.get('next')
    itemlist = product_cart.objects.filter(user_id=request.user.id, product_id=prodid, pharmacy_name=docid)
    if len(itemlist) > 0:
        ob = itemlist[0]
        if ob.quntity != 0:
            ob.quntity += 1
            ob.save()

    return redirect('medicine_cart')
def delete(request):
    prodid = request.GET.get('id')
    docid = request.GET.get('next')
    itemlist = product_cart.objects.filter(user_id=request.user.id, product_id=prodid, pharmacy_name=docid)
    itemlist.delete()
    print(prodid,'ppp',docid,itemlist)
    return redirect('medicine_cart')
def payment_success(request):
    userid = request.GET.get('user')
    return render(request,'pharmacy/payment-success.html')
def product_checkout(request):
    itemlist = product_cart.objects.filter(user_id=request.user.id)
    li=[]
    total=0
    # total=0
    dic={}
    for data in itemlist:
        pharmacy_id = data.pharmacy_name
        prodct_id = data.product_id
        products = pha_product.objects.get(id=prodct_id)
        allprice = products.price * data.quntity
        total += allprice
        if products.quntity < data.quntity:
            messages.success(request, 'product quntity is less')
        else:
            li.append([products, allprice, data.quntity])
        sub = total + 25  # shippnig/tax
        all =(sub-(sub * (products.discount / 100)))
        dic = {'product': li, 'total': total,'sub':sub, 'alltotal': int(all),'dis':products.discount}
    return render(request,'pharmacy/product-checkout.html',dic)
def product_order(request):
    itemlist = product_cart.objects.filter(user_id=request.user.id)
    li = []
    total = 0
    for data in itemlist:
        pharmacy_name = data.pharmacy_name
        product_id = data.product_id
        products = pha_product.objects.get(id=product_id)
        allprice = products.price * data.quntity
        total+=allprice
        li.append([products, allprice, data.quntity])
        sub = total + 25  # shippnig/tax
        # all = (sub - (sub * (products.discount / 100)))
        # print(all,'allllll',sub,total)
        if products.quntity <data.quntity:
            messages.warning(request, ' You can\'t buy this product bcz product quntity is less')
        else:
            if request.method == "POST":
                contact_no = request.POST['phone']
                address = request.POST['address']
                shipping = request.POST['shipping']
                cardname = request.POST['card_name']
                cardno = request.POST['card_no']
                cvv= request.POST['cvv']
                expyear = request.POST['exp_year']
                expmonth = request.POST['exp_month']
                var = pharmacy_prod_order(username=request.user.username,phone=contact_no,address=address,
                                          shipping_details=shipping,card_name=cardname,card_no=cardno,
                                          exp_month=expmonth,exp_year=expyear,cvv=cvv,product_id=products,
                                          pharmacys=products.doc,price=products.price,total=sub,product_name=products.name,
                                          quntitys=data.quntity,invoice=0)
                var.save()
                prods = pha_product.objects.filter(id=data.product_id)
                qunt=products.quntity-data.quntity
                if len(prods)>0:
                    ob=prods[0]
                    ob.quntity=qunt
                    ob.save()
                # messages.success(request, 'Order placed successfully ')
            data.delete()
    #
    messages.success(request, 'Order placed successfully ')
    return redirect('payment_success')