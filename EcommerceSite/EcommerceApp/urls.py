from django.urls import path
from .views import CartDetail, ListCart, ListCategory,ListProduct,ProductDetails,ListBooks,BookDetails,ListUser,UserDetails


urlpatterns = [
    path('category',ListCategory.as_view(),name='category'),
    path('category/<int:pk>',ListCategory.as_view(),name='singlecategory'),
    path('product',ListProduct.as_view(),name='product'),
    path('product/<int:pk>',ProductDetails.as_view(),name='singleproduct'),
    path('book',ListBooks.as_view(),name='book'),
    path('book/<int:pk>',BookDetails.as_view(),name='singlebook'),
    path('user',ListUser.as_view(),name='user'),
    path('user/<int:pk>',UserDetails.as_view(),name='singleuser'),
    path('cart',ListCart.as_view(),name='cart'),
    path('cart',CartDetail.as_view(),name='singlecart')
]
