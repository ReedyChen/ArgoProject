from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.urls import path

from . import views



app_name = 'applications'
urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    #url(r'^apply$', login_required(views.ApplyView.as_view()), name='apply'),

    

]
