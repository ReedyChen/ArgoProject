from django.conf.urls import url
#import cas.middleware

from . import views

app_name = 'appauth'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^login/forgetpassword/$', views.forgetPassword, name='forgetpassword'),
    url(r'^login/forgetpasswordview/$', views.forgetPasswordView, name='forgetpasswordview'),
    url(r'^resetpassword/(?P<key>\w+)/$', views.resetPage, name='resetpasswordview'),
    url(r'^resetpassword/change/(?P<key>\w+)/$', views.resetPassword, name='resetpassword'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^passwordpage/$', views.changePasswordView, name='passwordpage'),
    url(r'^passwordpage/changepassword/$', views.changePassword, name='changepassword'),
	url(r'^register/confirm/(?P<key>\w+)/$',views.confirm, name='confirm'),
]
