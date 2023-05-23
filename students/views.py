from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .forms import CreateStudent,ProjetForm
from django.db.models import Count, Avg, Min, Max
from .models import ProjectView


# Create your views here.
def student_list(request):
    students = StudentInfo.objects.all()
    paginator = Paginator(students, 1)
    page = request.GET.get('page')
    paged_students = paginator.get_page(page)

    context = {
        "students": paged_students
    }
    return render(request, "students/student_list.html", context)


def single_student(request, student_id):
    single_student = get_object_or_404(StudentInfo, pk=student_id)
    context = {
        "single_student": single_student
    }
    return render(request, "students/student_details.html", context)


def student_regi(request):
    if request.method == "POST":
        forms = CreateStudent(request.POST)

        if forms.is_valid():
            forms.save()
        messages.success(request, "Student Registration Successfully!")
        return redirect("student_list")
    else:
        forms = CreateStudent()

    context = {
        "forms": forms
    }
    return render(request, "students/registration.html", context)


def edit_student(request, pk):
    student_edit = StudentInfo.objects.get(id=pk)
    edit_forms = CreateStudent(instance=student_edit)

    if request.method == "POST":
        edit_forms = CreateStudent(request.POST, instance=student_edit)

        if edit_forms.is_valid():
            edit_forms.save()
            messages.success(request, "Edit Student Info Successfully!")
            return redirect("student_list")

    context = {
        "edit_forms": edit_forms
    }
    return render(request, "students/edit_student.html", context)


def delete_student(request, student_id):
    student_delete = StudentInfo.objects.get(id=student_id)
    student_delete.delete()
    messages.success(request, "Delete Student Info Successfully")
    return redirect("student_list")


def attendance_count(request):
    class_name = request.GET.get("class_name", None)
    if class_name:
        student_list = StudentInfo.objects.filter(class_type__class_short_form=class_name)
        context = {"student_list": student_list}
    else:
        context = {}
    return render(request, "students/attendance_count.html", context)
#projet


def projet_list(request):
    projets = Projet.objects.all()
    
    paginator = Paginator(projets, 1)
    page = request.GET.get('page')
    paged_projets = paginator.get_page(page)

    context = {
        "projets": paged_projets
    }
    return render(request, "projets/projet_list.html", context)


def single_projet(request, projet_id):
    single_projet = get_object_or_404(Projet, pk=projet_id)
    context = {
        " single_projet":  single_projet
    }
    return render(request, "projets/projet_details.html", context)


def projet_regi(request):
    if request.method == "POST":
        forms = ProjetForm(request.POST, request.FILES or None)

        if forms.is_valid():
            forms.save()
        messages.success(request, "Projet Registration Successfully!")
        return redirect("projet_list")
    else:
        forms = ProjetForm()

    context = {
        "forms": forms
    }
    return render(request, "projets/registration.html", context)


def edit_projet(request, pk):
    projet_edit = Projet.objects.get(id=pk)
    edit_form = ProjetForm(instance=projet_edit)

    if request.method == "POST":
        edit_form = ProjetForm(request.POST, request.FILES or None, instance=projet_edit)

        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, "Edit Projet Info Successfully!")
            return redirect("projet_list")

    context = {
        "edit_form": edit_form
    }
    return render(request, "projets/edit_projet.html", context)


def delete_projet(request, projet_id):
    projet_delete = Projet.objects.get(id=projet_id)
    projet_delete.delete()
    messages.success(request, "Delete projet Info Successfully")
    return redirect("projet_list")



def popular_projects(request):
    project_count = Projet.objects.count()
    total_views = ProjectView.objects.count()
    avg_views_per_project = total_views / project_count if project_count > 0 else 0

  
    min_views_project = Projet.objects.annotate(min_views=Min('views__timestamp')).order_by('min_views').first()
    max_views_project = Projet.objects.annotate(max_views=Max('views__timestamp')).order_by('-max_views').first()

    context = {
        'project_count': project_count,
        'total_views': total_views,
        'avg_views_per_project': avg_views_per_project,
        'projects': projects,
        'min_views_project': min_views_project,
        'max_views_project': max_views_project,
    }
    return render(request, 'projets/popular_projects.html', context)



#client
from django.shortcuts import render, redirect
from .models import Projet,  Equipe, ProjectRequest
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})

@staff_member_required
def project_requests(request):
    requests = ProjectRequest.objects.all()
    return render(request, 'clients/project_requests.html', {'requests': requests})

@staff_member_required
def approve_project_request(request, request_id):
    project_request = ProjectRequest.objects.get(id=request_id)
    project_request.status = 'APPROVED'
    project_request.save()
    return redirect('project_requests')

@staff_member_required
def reject_project_request(request, request_id):
    project_request = ProjectRequest.objects.get(id=request_id)
    project_request.status = 'REJECTED'
    project_request.save()
    return redirect('project_requests')


  #reigter client 

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import ClientInscriptionForm, PersonnelInscriptionForm, ConnexionForm
from .models import Client, Personnel

def inscription_client(request):
    if request.method == 'POST':
        form = ClientInscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion_client')
    else:
        form = ClientInscriptionForm()
    return render(request, 'inscription_client.html', {'form': form})

def inscription_personnel(request):
    if request.method == 'POST':
        form = PersonnelInscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion_personnel')
    else:
        form = PersonnelInscriptionForm()
    return render(request, 'inscription_personnel.html', {'form': form})

def connexion_client(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accueil')
    else:
        form = ConnexionForm()
    return render(request, 'connexion_client.html', {'form': form})

def connexion_personnel(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accueil')
    else:
        form = ConnexionForm()
    return render(request, 'connexion_personnel.html', {'form': form})


#demande projet
from django.shortcuts import render, redirect
from .forms import DemandeProjetForm

def demande_projet(request):
    if request.method == 'POST':
        form = DemandeProjetForm(request.POST)
        if form.is_valid():
            # Traitement de la demande de projet
            libelle = form.cleaned_data['libelle']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            
            # Sauvegarde de la demande de projet dans la base de données
            # (vous devez avoir un modèle correspondant pour cela)
            projet = Projet(libelle=libelle, description=description, image=image)
            projet.save()
            
            return redirect('accueil')  # Rediriger vers la page d'accueil après soumission réussie
    else:
        form = DemandeProjetForm()
    
    return render(request, 'projets/demande_projet.html', {'form': form})


def reception_demande_projet(request):
    # Récupérer les demandes de projet non traitées
    demandes_projet = Projet.objects.filter(acheve=False)
    
    return render(request, 'reception_demande_projet.html', {'demandes_projet': demandes_projet})



#--------------------------------------------------DEMANDE PROJETS------------------------------------------------------------------
@login_required
def demande_projet(request):
    if request.method == 'POST':
        form = DemandeProjetForm(request.POST, request.FILES)
        if form.is_valid():
            demande_projet = form.save(commit=False)
            if request.user.is_authenticated:
                client = Client.objects.get(user=request.user)
                demande_projet.client = client
                demande_projet.save()
                messages.success(request, 'Votre demande de projet a été soumise avec succès.')
                return redirect('projet')
            else:
                messages.error(request, 'Vous devez être connecté pour soumettre une demande de projet.')
    else:
        form = DemandeProjetForm()
    return render(request, 'artyweb/demandeprojet/demande_projet.html', {'form': form})

def demande_projet_list(request):
    demandes_projet = DemandeProjet.objects.all()
    return render(request, 'artyweb/demandeprojet/demande_projet_list.html', {'demandes_projet': demandes_projet})




    #------------------------------------------------CONFIRMER/PAYMENT-------------------------------------------------------------------------
@login_required
def confirmer_commande(request):
    panier = Panier.objects.get(user=request.user)
    total = panier.total_prix
    # Configuration pour PayPal
    paypal_dict = {
        'business': request.user.email,
        'amount': total,
        'currency_code': 'DT',
        'item_name': 'Formation sur ArtiWeb',
    }
    # Créer le formulaire PayPal et renvoyer le HTML pour le bouton de paiement
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {
        'form': form,
        'total': total,
    }
    return render(request, 'artyweb/panier/confirmer_commande.html', context)

#---------------------------------------------------CRUD DEMANDE PROJET-----------------------------------------------------------------
def modifier_demande_projet(request, demande_projet_id):
    demande_projet = get_object_or_404(DemandeProjet, id=demande_projet_id)
    if request.method == 'POST':
        form = DemandeProjetEditForm(request.POST, instance=demande_projet)
        if form.is_valid():
            form.save()
            return redirect('demande_projet_list')
    else:
        form = DemandeProjetEditForm(instance=demande_projet)
    return render(request, 'artyweb/demandeprojet/modifier_demande_projet.html', {'form': form})

def supprimer_demande_projet(request, demande_projet_id):
    demande_projet = get_object_or_404(DemandeProjet, id=demande_projet_id)
    demande_projet.delete()
    return redirect('demande_projet_list')