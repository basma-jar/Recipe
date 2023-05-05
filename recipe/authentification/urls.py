from django.urls import path
from .views import signup,login_view,logout_view

urlpatterns = [
    path('signUp/', signup, name='signUp'),
    path('signIn/', login_view, name='signIn'),
    
    path('logout/', logout_view, name='logout'),
]   