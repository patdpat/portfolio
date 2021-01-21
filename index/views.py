from django.http import HttpResponse
from django.template import loader,RequestContext
from django.shortcuts import render
from .models import Enquiry
from .forms import EnquiryForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):
  form = EnquiryForm()
  return render(request, 'index/index.html', {'form': form})
@csrf_exempt
def add_enquiry(request):
  form = EnquiryForm()
  one= request.POST['name']
  two=request.POST['email']
  three =request.POST['message']
  Enquiry.objects.create(name=one,email=two,message=three)
  return render(request, 'index/index.html', {'form': form})
