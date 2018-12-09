from django.conf.urls import url

from baisc_app import views

app_name='baisc_app'

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login')
]