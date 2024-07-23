from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    Name=models.CharField(max_length=255)
    ContactNo=models.CharField(max_length=20)
    EmailId=models.EmailField(max_length=255)
    Salary=models.IntegerField()
    Address=models.TextField()

    def __str__(self):
        return self.Name

class Student(models.Model):
    Name=models.CharField(max_length=255)
    ContactNo=models.CharField(max_length=20)
    RollNo=models.IntegerField()
    EmailId=models.EmailField(max_length=255)
    DOB=models.DateField()
    CourseName=models.CharField(max_length=100)
    CityName=models.CharField(max_length=100)
    Address=models.TextField()
    Pincode=models.IntegerField()
    FatherName=models.CharField(max_length=255)
    MotherName=models.CharField(max_length=255)
    
    def __str__(self):
        return self.Name
    
class Enquiry(models.Model):
    Name=models.CharField(max_length=255)
    ContactNo=models.CharField(max_length=20)
    EmailId=models.EmailField(max_length=255)
    userid=models.ForeignKey(User,on_delete=models.CASCADE, default=0)
    City=models.CharField(max_length=100)
    Message=models.TextField()
    Pic=models.ImageField(upload_to='media')
    Enquiry_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Name

class Category(models.Model):
    Name= models.CharField(max_length=100)
    Image=models.ImageField()
    Status=models.BooleanField()

    def __str__(self):
        return self.Name

class SubCategory(models.Model):
    Name=models.CharField(max_length=100)
    Catid=models.ForeignKey(Category, on_delete=models.CASCADE)
    Image=models.ImageField()

    def __str__(self):
        return self.Name
    
class Product(models.Model):
    ProductName=models.CharField(max_length=100)
    Producttitle=models.CharField(max_length=255)
    Image=models.ImageField()
    MRP=models.DecimalField(max_digits=6, decimal_places=2)
    Discount=models.DecimalField(max_digits=6, decimal_places=2)
    salesprice=models.DecimalField(max_digits=6, decimal_places=2)
    Quanity=models.IntegerField()
    Description=models.TextField()
    Status=models.BooleanField()
    Catid=models.ForeignKey(Category, on_delete=models.CASCADE)
    Subcatid=models.ForeignKey(SubCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.ProductName
    
class usercart(models.Model):
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    pid=models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity=models.IntegerField(default=1)
    entrydate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart Added"
    
class slider(models.Model):
    backgroundimage=models.ImageField()
    sliderimage=models.ImageField()
    sliderheading= models.CharField(max_length=255)
    slidercontent=models.TextField()
    isactive=models.CharField(max_length=20,  null=True)

    def __str__(self):
        return self.sliderheading
    
class Country(models.Model):
    Name= models.CharField(max_length=215)

    def __str__(self):
        return self.Name

class State(models.Model):
    Name=models.CharField(max_length=215)
    cid=models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
    
class City(models.Model):
    Name=models.CharField(max_length=100)
    sid=models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
    
class checkout(models.Model):
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    addline1=models.CharField(max_length=250,default=0)
    addline2=models.CharField(max_length=250,default=0)
    contact=models.CharField(max_length=20,default=0)
    country=models.IntegerField()
    state=models.IntegerField()
    city=models.IntegerField()
    pincode=models.IntegerField()

    def __str__(self):
        return self.userid.first_name
    
class OrderedItems(models.Model):
    userid=models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    pids=models.ForeignKey(Product, on_delete=models.CASCADE,default=0)
    totalamt=models.CharField(max_length=255)
    quanity=models.IntegerField(default=1)
    payment_mode=models.CharField(max_length=100)
    order_status=models.CharField(max_length=100)
    order_date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.pids.ProductName