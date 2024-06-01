from django.shortcuts import render
from django.views import View
from .models import *
from django.views.generic.edit import CreateView

# Create your views here.

class Myview(View):
    def get(self,request):
        return render(request,'html/test.html')

class GreekCreate(CreateView):
    model = GeeksModel
    fields = '__all__'



