from django.urls import path
from apps import views
app_name='apps'
urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login')
]
