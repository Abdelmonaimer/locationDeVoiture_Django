from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import PatientForm, CarsForm, EmployeesForm
from .models import Patient, Voiture, Employee
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


def cars_dash(request):
    for i in range(0):
        v = Voiture(
            marque=f.word(),
            modele=f.word(),
            type=f.word(),
            color=f.word(),
            doors=f.random_int(),
            image=f.word(),
            seats=f.random_int(),

        )
        v.save()
    cars = Voiture.objects.all()
    paginator = Paginator(cars, 10)
    page = request.GET.get('page', 1)
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)
    return render(request, "cars_dash.html", {'cars': cars})


def add_car(request):
    if request.method == 'POST':
        form = CarsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cars_dash')
    else:
        form = CarsForm()
    return render(request, 'add_car.html', {'form': form})


def update_car(request, pk):
    car = get_object_or_404(Voiture, pk=pk)
    if request.method == 'POST':
        form = CarsForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('cars_dash')
    else:
        form = CarsForm(instance=car)
    return render(request, 'update_car.html', {'form': form, 'car': car})


def delete_car(request, pk):
    voiture = get_object_or_404(Voiture, pk=pk)

    voiture.delete()
    return redirect('cars_dash')


def employees_dash(request):
    for i in range(0):
        e = Employee(
            nom=f.name(),
            username=f.word(),
            password=f.word(),
            role=f.word(),

        )
        e.save()
    employees = Employee.objects.all()
    return render(request, "Employees_dash.html", {'employees': employees})


def add_employee(request):
    if request.method == 'POST':
        form = EmployeesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees_dash')
    else:
        form = EmployeesForm()
    return render(request, 'add_employee.html', {'form': form})


def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeesForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees_dash')
    else:
        form = EmployeesForm(instance=employee)
    return render(request, 'update_employee.html', {'form': form, 'employee': employee})


def delete_employees(request, pk):
    employees = get_object_or_404(Employee, pk=pk)

    employees.delete()
    return redirect('employees_dash')


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def contact(request):
    return render(request, "contact.html")
