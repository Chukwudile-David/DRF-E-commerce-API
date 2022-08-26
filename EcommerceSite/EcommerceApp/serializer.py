from unicodedata import category
from rest_framework import serializers
from .models import category,Book,Product,Cart
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = category
        fields = (
            'id',
            'title')

class BookSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source = 'created_by.username')


    class Meta:
        model = Book
        fields = (
        'id',
        'title',
        'category',
        'author',
        'Isbn',
        'pages',
        'price',
        'stock',
        'description',
        'imageurl',
        'created_by',
        'status',
        'date_created')


class ProductSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source = 'created_by.username')


    class Meta:
        model = Product
        fields = (
        'id',
        'product_tag',
        'name',
        'category',
        'price',
        'stock',
        'imageurl',
        'created_by',
        'status',
        'date_created')

class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True,queryset = Book.objects.all())
    products = serializers.PrimaryKeyRelatedField(many=True,queryset = Product.objects.all())

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'books',
            'products',
        )

class UserinfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )

class CartSerializer(serializers.ModelSerializer):
    cart_id = UserinfoSerializer(read_only = True, many = False)
    books = BookSerializer(read_only = True, many = True)
    products = ProductSerializer(read_only = True, many = True)

    class Meta:
        model = Cart 
        fields = (
            'cart_id',
            'created_at',
            'products',
            'books',
        )

class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50,min_length= 9)
    username = serializers.CharField(max_length = 50,min_length= 9)
    password = serializers.CharField(write_only = True,max_length = 150,min_length= 9)

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'password',

        )

    def validate(self, args):
        email = args.get('email',None)
        username = args.get('username',None)

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username':('username already taken')})

        return super().validate(args)

        

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)