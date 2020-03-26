
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.conf import settings
from django.views.static import serve
from django.shortcuts import render
from forms_builder.forms.models import Form


urlpatterns = [
    url(r'^$', lambda request: render(request, "index.html", {"forms": Form.objects.all()})),
                                         
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('appauth.urls')),
    url(r'^forms/', include('forms.urls')),
    url(r'^applications/', include('applications.urls')),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    #url(r'^message$', sendMessage, name='message'),
    
]
