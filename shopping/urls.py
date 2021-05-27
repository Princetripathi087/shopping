from django.urls import path
from . import views
urlpatterns = [
    path('index.html',views.index,name='index'),
    path('account.html',views.account,name='account'),
    path('cart.html',views.cart,name='cart'),
    path('electronics.html',views.electronics,name='electronics'),
    path('elecspc.html/<int:i>/',views.elecspc,name='elecspc'),
    path('mobile.html',views.mobile,name='mobile'),
    path('oneplus.html/<int:mid>/',views.oneplus,name='oneplus'),
    #path('product.html',views.product,name='product'),
    path('Products.html',views.Product,name='Products'),
    path('redmi.html',views.redmi,name='redmi'),
    path('register.html',views.register,name='register'),
    path('samsung.html',views.samsung,name='samsung'),
    path('signin.html',views.signin,name='signin'),
]