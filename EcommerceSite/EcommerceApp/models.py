from tkinter import CASCADE
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class category(models.Model):
    title = models.CharField(max_length=100,)
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(category,related_name='books',on_delete=models.CASCADE)
    author = models.CharField(max_length=100, default='John Doe')
    Isbn = models.CharField(max_length=100)
    pages = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    imageurl = models.URLField()
    created_by = models.ForeignKey('auth.user', related_name='books',on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

class Product(models.Model):
    product_tag = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(category,related_name='products',on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageurl = models.URLField()
    created_by = models.ForeignKey('auth.user', related_name='products',on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return '{} {}'.format(self.product_tag,self.name)

class Cart(models.Model):
    cart_id =  models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    created_at =models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)
    books = models.ManyToManyField(Book)
    class Meta:
        ordering = ['cart_id','created_at']

    def __str__(self):
        return str(self.cart_id)


    





