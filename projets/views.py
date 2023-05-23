''''from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .forms import ProjetForm
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
    single_projet = get_object_or_404(StudentInfo, pk=projet_id)
    context = {
        " single_projet":  single_projet
    }
    return render(request, "projets/projet_details.html", context)


def projet_regi(request):
    if request.method == "POST":
        forms = ProjetForm(request.POST)

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
        edit_form = ProjetForm(request.POST, instance=projet_edit)

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

'''