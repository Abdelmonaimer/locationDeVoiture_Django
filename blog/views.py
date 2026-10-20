import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .decorators import unauthenticated_user, allowed_users
from .forms import PatientForm, CarsForm, EmployeesForm, CreateUserForm, ClientsForm, ReservationForm
from .models import Patient, Voiture, Employee, Client, Reservation, Facture
from faker import Faker

import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


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


@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    return render(request, "register.html", {'form': form})


@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars_dash')
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, "login.html", {})


def logoutUser(request):
    logout(request)
    return redirect('login')


def home2(request):
    car = Voiture.objects.last() # hadi bach kanjibo akhir insertion fla classe Voiture (table voiture f database) stockinaha f variable smitha car
    cars = Voiture.objects.all() # hadi bach kanjibo ga3 les insertions (ga3 rows) fla classe Voiture (table voiture f database) stockinaha f variable smitha cars
    context = {
        'car': car,
        'cars': cars,
    } # context 7tina fiha les variables li lfo9 bach nseftohom l page html index.html
    return render(request, "index.html", context) # return render seftna fiha les parametres ## hadi hya lview dyal page home


def services(request):
    return render(request, "services.html") ## view dyal page services and since its static drna fiha ghi return dyal page html


def cars(request):
    car_list = Voiture.objects.all() ## same as above stockina ga3 lcars li 3ndna f database f variable car_list
    return render(request, "cars.html", {'car_list': car_list}) ## again seftnahaa f parameter


@login_required(login_url='login') ## hadi kadirha fo9 ay page mabghitihch ydkhol liha bla login i mean blama ykon connected dakshi 3lash smitha login_required
@allowed_users(allowed_roles=['admin', 'manager']) # hadi bghina dashboard y9dr ydkhol lih gha admin w manager ila kan chi user maydkholch allowed_users
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

        ) ## hada ghir faker knt dkhlt biha fake data bach ntesti so nevermind
        v.save() ## dave data f databse gha dyal faker hadi so nvm 2
    cars = Voiture.objects.all() ## fhmtoha yak ?
    paginator = Paginator(cars, 4)
    page = request.GET.get('page', 1)
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages) ## had lcode li lfo9 kaml dyal paginator howa bach kandiro pagination tbh mafahmoch mzyn ila swlna angolo lih 3titih lina f cours drna bhalo wsf
    return render(request, "cars_dash.html", {'cars': cars})


@login_required(login_url='login') ## same as above hadi kandiroha k ay haja requires the login
@allowed_users(allowed_roles=['admin', 'manager'])
def add_car(request):
    if request.method == 'POST': ## had if drnaha and it means ila drti submit l form 3ad tadir hadshi li lt7t
        form = CarsForm(request.POST, request.FILES) ## hadi 7tina fiha lform li drna f forms.py normally hadi tatkon fiha request.post f parametre ms hadi zdna fiha ta dik request.FILE 3la wed insertion dyal image flcar
        if form.is_valid(): ## ila kant lform valid (les champs 3amrin etc..) ghaydir hadshi li lt7t
            form.save() ## method .save() kayna f django tatsavi lik dok data li jaw flform f database
            return redirect('cars_dash') ## mn b3d kaydik l dashboard tl cars tani hya "cars_dash"
    else:
        form = CarsForm() ## else ila makanch dakshi valid taykhlik f nfs lform again
    return render(request, 'add_car.html', {'form': form})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'manager'])
def update_car(request, pk): ## hna normalement tansefto gha request but since bghina ndiro edit f data aykhsna l id dyal hadik li bina n editiw
    car = get_object_or_404(Voiture, pk=pk) ## variable 7tina fiha dik lcar li jbna bl id dyalha
    if request.method == 'POST': ## again ila t submita dakshi
        form = CarsForm(request.POST, request.FILES, instance=car) ## hna tani tanjibo lform mn forms.py o tanzido wahd instance car bach tatji lform 3amra b data (car) nta katbdl gha dik li bghiti
        if form.is_valid():
            form.save()
            return redirect('cars_dash')
    else:
        form = CarsForm(instance=car)
    return render(request, 'update_car.html', {'form': form, 'car': car})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'manager'])
def delete_car(request, pk):
    voiture = get_object_or_404(Voiture, pk=pk)

    voiture.delete() ## had lview same as update tatjib id (li howa pk) w tadir fonction
    return redirect('cars_dash')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def employees_dash(request):
    for i in range(0):
        e = Employee(
            nom=f.name(),
            username=f.word(),
            password=f.word(),
            role=f.word(),

        )
        e.save()
    employees = Employee.objects.all() ## dashboard dyal les employees bhaaalo bhal cars tayjibhom kamlin o tay7thom lik
    return render(request, "Employees_dash.html", {'employees': employees})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_employee(request):
    if request.method == 'POST':
        form = EmployeesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees_dash')
    else:
        form = EmployeesForm()
    return render(request, 'add_employee.html', {'form': form})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_employees(request, pk):
    employees = get_object_or_404(Employee, pk=pk)

    employees.delete()
    return redirect('employees_dash')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'manager'])
def clients_dash(request):
    for i in range(0):
        c = Client(
            nom=f.name(),
            prenom=f.name(),
            email=f.email(),
            username=f.word(),
            password=f.word(),

        )
        c.save()
    clients = Client.objects.all()
    paginator = Paginator(clients, 8)
    page = request.GET.get('page', 1)
    try:
        clients = paginator.page(page)
    except PageNotAnInteger:
        clients = paginator.page(1)
    except EmptyPage:
        clients = paginator.page(paginator.num_pages)
    return render(request, "clients_dash.html", {'clients': clients})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'manager'])
def update_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientsForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients_dash')
    else:
        form = ClientsForm(instance=client)
    return render(request, 'update_client.html', {'form': form, 'client': client})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'manager'])
def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)

    client.delete()
    return redirect('clients_dash')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'manager'])
def manager_dash(request):
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
    return render(request, "manager_dash.html", {'cars': cars})


@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])
def reservations_dash(request):
    for i in range(0):
        r = Reservation(
            dateDebut=f.date(),
            dateFin=f.date(),
            prix=f.random_int(),

        )
        r.save()
    reservations = Reservation.objects.all()
    paginator = Paginator(reservations, 8)
    page = request.GET.get('page', 1)
    try:
        reservations = paginator.page(page)
    except PageNotAnInteger:
        reservations = paginator.page(1)
    except EmptyPage:
        reservations = paginator.page(paginator.num_pages)
    return render(request, "reservation_dash.html", {'reservations': reservations})


@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])
def update_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservations_dash')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'update_reservation.html', {'form': form, 'reservation': reservation})


def reserver_car(request, pk):
    car = get_object_or_404(Voiture, pk=pk) ## jbna voiture li bghina nreserviw bl id dyalha (pk)
    if request.method == 'POST':
        form = CarsForm(request.POST, request.FILES, instance=car)
        date_format = "%Y-%m-%d" ## drna wahd lformat li ghatrespectiha dik la date li ghanjibo
        dateDebut = datetime.datetime.strptime(str(request.POST.get('dateDebut')), date_format)
        dateFin = datetime.datetime.strptime(str(request.POST.get('dateFin')), date_format)
        diff = dateFin - dateDebut ## differnce entre les dates
        prix = request.POST.get('prix') ## post.get jabt lina data li dkhlna f input dyal les prix
        montant = int(diff.days) * int(prix)
        fac = Facture(
            nbrJours=float(diff.days),
            nom=request.POST.get('nom'),
            prenom=request.POST.get('prenom'),
            montant=float(montant)

        ) ## hadi drna instance bhaal dik dyal faker , w drna columns dyal table y3mro b dakshi li 7sbna lfo9
        facture = Facture.objects.last()
        r = Reservation(
            dateDebut=request.POST.get('dateDebut'),
            dateFin=request.POST.get('dateFin'),
            prix=request.POST.get('prix'),
            voiture_id=request.POST.get('voiture'),
            facture_id=facture.id + 1

        )
        rsv = Reservation.objects.last()
        client = Client(
            nom=request.POST.get('nom'),
            prenom=request.POST.get('prenom'),
            email=request.POST.get('email'),
            facture_id=facture.id + 1,
            reservation_id=rsv.id + 1

        )

        if form.is_valid():
            form.save()
            fac.save()
            r.save()
            client.save()
            return redirect('cars')
    else:
        form = CarsForm(instance=car)
    return render(request, 'reserver.html', {'form': form, 'car': car})


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }

        message = '''
         New message: {} 
         From: {}
         '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['Autogo300@gmail.com'])
    return render(request, "contact.html", {})


def facture_pdf(request, pk):
    # buffer
    buf = io.BytesIO()
    # canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # text object
    text_ob = c.beginText()
    text_ob.setTextOrigin(inch, inch)
    text_ob.setFont("Helvetica", 14)
    rsv = Reservation.objects.filter(id=pk)
    # lines of text
    lines = []
    for r in rsv:
        lines.append(
            "Agence AutoGo                                                              " + str(datetime.date.today()))
        lines.append("  ")
        lines.append("  ")
        lines.append("  ")
        lines.append("  Facture Num : " + str(r.facture.id))
        lines.append("  ")
        lines.append("  CLIENT : " + r.facture.nom + "   " + r.facture.prenom)
        lines.append("  ")
        lines.append("  ")
        lines.append("  VOITURE Reservée :      " + r.voiture.marque + " " + r.voiture.modele)
        lines.append("                  type  :   " + r.voiture.type + " couleur : " + r.voiture.color)
        lines.append("                  doors :   " + str(r.voiture.doors) + " seats : " + str(r.voiture.seats))
        lines.append("  ")
        lines.append("  ")
        lines.append("  Durée de         :     " + str(r.facture.nbrJours) + " Jours.")
        lines.append("                  du    :     " + str(r.dateDebut) + " au :" + str(r.dateFin))
        lines.append("  ")
        lines.append("  ")
        lines.append("  ")
        lines.append("  ")
        lines.append("  Prix en MAD/jour :" + str(r.prix) + "                          Montant total en MAD : " + str( r.facture.montant))
        lines.append(" ")

    # loop
    for line in lines:
        text_ob.textLine(line)
    # finish up
    c.drawText(text_ob)
    c.showPage()
    c.save()
    buf.seek(0)
    # return
    return FileResponse(buf, as_attachment=True, filename='facture.pdf')
