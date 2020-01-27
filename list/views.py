from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from django.http import HttpResponse
from . models import Admission, Item

# Create your views here.
def index(request):
	return render(request,'list/index.html')


def create_new_admission(request):
	return HttpResponse("this is create new admission form")



class AdmissionListView(ListView):
	model = Admission
	template_name = "list/index.html"
	context_object_name = 'admissions'

class AdmissionDetailView(DetailView):
	model = Admission
	
