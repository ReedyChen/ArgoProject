from django.shortcuts import render
from django import views
from .models import *



# Create your views here.
class IndexView(views.generic.ListView):
    template_name = 'applications/index.html'
    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data(**kwargs)

        return ctx
    def get_queryset(self):
        return Application.objects.all()
