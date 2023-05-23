from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.http import  HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Service
from .forms import ServiceForm
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.
def employee_list(request):
    official_info = OfficialInfo.objects.all()
    context = {
        "official_info": official_info
    }
    return render(request, "employee/employee_list.html", context)


def create_employee(request):
    personal_info = PersonalInfo.objects.all()
    context = {
        "personal_info": personal_info
    }
    return render(request, "employee/registration.html", context)

#service
def service_list(request):
    services = Service.objects.all()

    paginator = Paginator(services, 1)
    page = request.GET.get('page')
    paged_services = paginator.get_page(page)
    context = {
        "services": paged_services
    }
    return render(request, "services/service_list.html", context)


def single_service(request, service_id):
    single_service = get_object_or_404(Service, pk=service_id)
    context = {
        "single_service": single_service
    }
    return render(request, "services/single_service.html", context)


def create_service(request):
    if request.method == "POST":
        forms = ServiceForm(request.POST, request.FILES or None)

        if forms.is_valid():
            forms.save()
        messages.success(request, "service Registration Successfully!")
        return redirect("service_list")
    else:
        forms = ServiceForm()

    context = {
        "forms": forms
    }
    return render(request, "services/create_service.html", context)


def edit_service(request, pk):
    service_edit = Service.objects.get(id=pk)
    edit_service_forms = ServiceForm(instance=service_edit)

    if request.method == "POST":
        edit_service_forms = ServiceForm(request.POST, request.FILES or None, instance=service_edit)

        if edit_service_forms.is_valid():
            edit_service_forms.save()
            messages.success(request, "Edit service Info Successfully!")
            return redirect("service_list")

    context = {
        "edit_service_forms": edit_service_forms
    }
    return render(request, "services/edit_service.html", context)


def delete_service(request, service_id):
    service_delete = Service.objects.get(id=service_id)
    service_delete.delete()
    messages.success(request, "Delete service Info Successfully")
    return redirect("service_list")












def search(request):
    query = request.GET.get('q')
    if query:
        services = Service.objects.filter(type__icontains=query)
        context = {'query': query, 'services': services}
        return render(request, 'services/search_result.html', context)
    else:
        return render(request, 'services/search_result.html')