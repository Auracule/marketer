from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= 'index'),
    path('contact/', views.contact, name = 'contact'),
    path('categories/', views.categories, name= 'categories'),
    path('category/<str:id>/<slug:slug>/', views.category, name= 'category'),
    path('product/', views.product, name='product'),
    path('search/', views.search, name='search'),
    path('single_prod/<str:id>/', views.single_prod, name= 'single_prod'),

    path('signin/', views.signin, name= 'signin'),
    path('signup/', views.signup, name= 'signup'),
    path('signout/', views.signout, name= 'signout'),

    path('profile/', views.profile, name='profile'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('password/', views.password, name='password'),
    
    path('cart/', views.cart, name='cart'),
    path('shopcart/', views.shopcart, name='shopcart'),
    path('delete_item/', views.delete_item, name='delete_item'),
    path('increase/', views.increase, name='increase'),

    path('checkout/', views.checkout, name='checkout'),
    path('pay/', views.pay, name='pay'),
    path('callback/', views.callback, name='callback'),
    path('history/', views.history, name='history'),
    path('del_history/', views.del_history, name='del_history'),
]
