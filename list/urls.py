from django.urls import path 

from . import views

app_name = 'list'

urlpatterns = [
	path('', views.AdmissionListView.as_view(), name = 'index'),
	path('<int:pk>/',views.AdmissionDetailView.as_view(), name='admissionDetail'),
	path('new/',views.create_new_admission, name='createNewAdmission'),
]