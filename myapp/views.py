from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import *
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import razorpay
# Create your views here.

def home(request):
    category=Category.objects.all()
    sliderdata=slider.objects.all()
    subcat={}
    for x in category:
        subcat[x]=SubCategory.objects.filter(Catid=x.id)[0:4]
    return render(request, 'home.html', {'category':category, 'sliderdata':sliderdata, 'subcat':subcat})

def about(request):
    return render(request, 'about us.html')

def contact(request):
    if request.method=="POST":
        f= Enquiryform(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            return redirect("display")
    return render(request, 'contact us.html')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

@login_required
def display(request):
    category=Category.objects.all()
    data=Enquiry.objects.filter(userid=request.user)
    if request.method=="POST":
        Name= request.POST['name']
        City= request.POST['city']
        data=Enquiry.objects.filter(userid=request.user, Name__icontains=Name, City__icontains=City)
    return render(request, 'display.html',{'data':data, 'category':category})

def deleterecord(request,id):
    data= Enquiry.objects.get(id=id)
    data.delete()
    return redirect('display')

def updateform(request,id):
    category=Category.objects.all()
    data= Enquiry.objects.get(id=id)
    if request.method=="POST":
        form= Enquiryform(request.POST, request.FILES, instance=data)
        form.save()
        return redirect("display") 
    return render(request, 'updaterecord.html',{'data':data, 'category':category})

def signupuser(request):
    if request.method=="POST":
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        email= request.POST['email']
        password= request.POST['password']
        username= request.POST['username']
        # userform=UserCreationForm(request.POST)
        newuser=User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        subject="Welcome To Our Project"
        message=f" Hello {first_name} ! Thanks for creating Account"
        sender=settings.EMAIL_HOST_USER
        receiver=[email]
        send_mail(subject, message, sender, receiver)
    return render(request,'Signup.html')

def loginuser(request):
    msg={}
    if request.method=="POST":
        username= request.POST['username']
        password= request.POST['password']
        user= authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('display')
        else:
            msg={'error': 'invaild username or password'}
    return render(request, 'Login.html', msg)

def logoutuser(request):
    logout(request)
    return redirect('login')

def subcategory(request, id):
    category=Category.objects.all()
    subcategory=SubCategory.objects.filter(Catid=id)
    return render(request, 'subcategory.html',{'subcat':subcategory, 'category':category}) 

def products(request, id):
    category=Category.objects.all()
    subcategory=SubCategory.objects.filter(Catid=id)
    products=Product.objects.filter(Subcatid=id)
    return render(request, 'product.html',{'subcat':subcategory, 'category':category, 'products':products}) 

def productdetails(request, id):
    product=Product.objects.get(id=id)
    return render(request, 'product-deatails.html',{'product':product})

@login_required
def addtocart(request):
    if request.method=="POST" :
        pid= request.POST.get('pid')
        product= get_object_or_404(Product, id=pid)
        cart, created= usercart.objects.get_or_create(userid=request.user, pid=product)
        if not created: 
            cart.Quantity+=1
            cart.save()
        return redirect('cart')    
        
def displaycart(request):
    cart=usercart.objects.filter(userid=request.user)
    total=0
    for x in cart:
        total+= x.pid.salesprice*x.Quantity
    return render(request, 'cart.html',{'cart':cart, 'total':total})

def deletecart(request, id):
    cart= usercart.objects.get(id=id)
    cart.delete()
    return redirect('cart')

def updatecart(request, id):
    cartdata= usercart.objects.get(id=id)
    if request.method=="POST":
        cartdata.Quantity=request.POST['Quantity']
        cartdata.save()
    return redirect('cart')

def checkoutPage(request):
    cart= usercart.objects.filter(userid=request.user.id)
    total=0
    for x in cart:
        total+=x.pid.salesprice*x.Quantity
    if (total<=500):
        sc=50
    else:
        sc=0
    gst=float(total)*0.18
    netamount=gst+float(total)+sc
    countrylist=Country.objects.all()
    context= {'country':countrylist, 'cart':cart, 'total':total, 'sc':sc,  'netamount':netamount }
    if request.method=="POST":
        data1= checkoutform(request.POST)
        data1.save()
        for p in cart:
            data2=OrderedItems()
            data2.userid= request.user
            data2. pids=p.pid
            data2.quanity=p.Quantity
            data2.totalamt=p.pid.salesprice*p.Quantity
            data2.payment_mode=request.POST.get('payment_mode')
            data2.order_status=('Pending')
            data2.save()
            cart.delete()
            newstock= p.pid.Quanity- p.Quantity
            product= Product.objects.get(id=p.pid.id)
            product.Quanity= newstock
            product.save()
        if request.POST.get('payment_mode')=="online":
            return render(request, 'payment.html', {'amount': int(netamount)*100})
        else:
            return render(request, 'success.html')
    return render(request,'purchaseform.html',context)

@csrf_exempt
def complete_payment(request):
    amount= request.POST.get('amount')
    client= razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
    razorpayorder= client.order.create(
        {"amount": int(amount)*100, 'currency':"INR", 'payment_capture':1}
    )
    return render(request, 'success.html')

def stateList(request):
    cid= request.GET.get('cid')
    stateList=State.objects.filter(cid=cid).values('id', 'Name')
    return JsonResponse(list(stateList), safe=False)

def cityList(request):
    sid= request.GET.get('sid')
    cityList=City.objects.filter(sid=sid).values('id', 'Name')
    return JsonResponse(list(cityList), safe=False)
