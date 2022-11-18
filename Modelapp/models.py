from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='name') 
    status = models.IntegerField(default=1) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='name') 
    status = models.IntegerField(default=1) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.DecimalField()
    discription = models.CharField()
    slug = AutoSlugField(populate_from='name') 
    is_feature = models.IntegerField(default=0) 
    on_sale = models.IntegerField(default=0) 
    status = models.IntegerField(default=1) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class UploadFiles(models.Model):
    product_type = models.IntegerField(default=1) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    otp = models.CharField(max_length=30)
    status = models.IntegerField(default=1) 
    slug = AutoSlugField(populate_from='name')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name