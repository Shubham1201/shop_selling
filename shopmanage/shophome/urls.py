from django.urls import path
from .views import *

urlpatterns = [
    path('', homeapp, name='homepage'),
    path('signup/', signUp, name='signup'),
    path('login/', logIn, name='login'),
    path('logout/', logOut, name='logout'),
    path('addshop/', addShop, name='addshop'),
    path('addentry/', addEntry, name='addentry'),
]