from django.conf.urls import url

from . import views

app_name = 'appauth'
urlpatterns = [
    # Sign up view
    url(r'^signup/$', views.signup, name='signup'), 

    # Login and forgetpassword views
    url(r'^login/$', views.user_login, name='login'),
    url(r'^login/forgetpassword/$', views.forgetPassword, name='forgetpassword'),
    url(r'^login/forgetpasswordview/$', views.forgetPasswordView, name='forgetpasswordview'),

    # Reset password views
    url(r'^resetpassword/(?P<key>\w+)/$', views.resetPage, name='resetpasswordview'),
    url(r'^resetpassword/change/(?P<key>\w+)/$', views.resetPassword, name='resetpassword'),

    # Log out
    url(r'^logout/$', views.user_logout, name='logout'),

    url(r'^passwordpage/$', views.changePasswordView, name='passwordpage'),
	url(r'^register/confirm/(?P<key>\w+)/$',views.confirm, name='confirm'),

    # Form creation page
    url(r'^createform/$',views.createformview.as_view(), name='createform'),
]
