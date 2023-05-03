from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PatientForm
from .models import Patient
from faker import Faker


# Create your views here.
def post_list2(request):
    posts = Patient.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_list(request):
    return HttpResponse("Hello, World")


f = Faker()


def patient_list(request):
    for i in range(0):
        p = Patient(
            nom=f.name(),
            dateNaissance=f.date(),
        )
        p.save()
    patient = Patient.objects.all()
    paginator = Paginator(patient, 10)
    page = request.GET.get('page', 1)
    try:
        patient = paginator.page(page)
    except PageNotAnInteger:
        patient = paginator.page(1)
    except EmptyPage:
        patient = paginator.page(paginator.num_pages)

    return render(request, 'patient_list.html', {'patient': patient})


def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'create_patient.html', {'form': form})


def update_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'update_patient.html', {'form': form, 'patient': patient})


def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('patient_list')


def search(request):
    query = request.GET.get('keyword')
    patient = Patient.objects.filter(nom__contains=query)
    return render(request, 'patient_list.html', {'patient': patient})


def home2(request):
    return render(request, "index.html")


def services(request):
    return render(request, "services.html")


def cars(request):
    return render(request, "cars.html")


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def contact(request):
    return render(request, "contact.html")
