from django.contrib import admin
from .models import category,Book,Product,Cart

# Register your models here.
admin.site.register(category)
admin.site.register(Book)
admin.site.register(Product)
admin.site.register(Cart)

