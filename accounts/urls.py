from django.urls import path

from .views import sign_up, login_user, logout_user

urlpatterns = [
    path('sign_up/', sign_up, name='sign_up'),
    path('', sign_up, name='sign_up'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user')
]