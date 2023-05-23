from django.shortcuts import render, get_object_or_404, redirect
from .models import TeacherInfo,Personnel
from .forms import CreateTeacher,PersonnelForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def teacher_list(request):
    teachers = TeacherInfo.objects.all()

    paginator = Paginator(teachers, 1)
    page = request.GET.get('page')
    paged_teachers = paginator.get_page(page)
    context = {
        "teachers": paged_teachers
    }
    return render(request, "teachers/teacher_list.html", context)


def single_teacher(request, teacher_id):
    single_teacher = get_object_or_404(TeacherInfo, pk=teacher_id)
    context = {
        "single_teacher": single_teacher
    }
    return render(request, "teachers/single_teacher.html", context)


def create_teacher(request):
    if request.method == "POST":
        forms = CreateTeacher(request.POST, request.FILES or None)

        if forms.is_valid():
            forms.save()
        messages.success(request, "Teacher Registration Successfully!")
        return redirect("teacher_list")
    else:
        forms = CreateTeacher()

    context = {
        "forms": forms
    }
    return render(request, "teachers/create_teacher.html", context)


def edit_teacher(request, pk):
    teacher_edit = TeacherInfo.objects.get(id=pk)
    edit_teacher_forms = CreateTeacher(instance=teacher_edit)

    if request.method == "POST":
        edit_teacher_forms = CreateTeacher(request.POST, request.FILES or None, instance=teacher_edit)

        if edit_teacher_forms.is_valid():
            edit_teacher_forms.save()
            messages.success(request, "Edit Teacher Info Successfully!")
            return redirect("teacher_list")

    context = {
        "edit_teacher_forms": edit_teacher_forms
    }
    return render(request, "teachers/edit_teacher.html", context)


def delete_teacher(request, teacher_id):
    teacher_delete = TeacherInfo.objects.get(id=teacher_id)
    teacher_delete.delete()
    messages.success(request, "Delete Teacher Info Successfully")
    return redirect("teacher_list")

#personneelll

def personnel_list(request):
    personnels = Personnel.objects.all()

    paginator = Paginator(personnels, 1)
    page = request.GET.get('page')
    paged_personnels = paginator.get_page(page)
    context = {
        "personnels": paged_personnels
    }
    return render(request, "personnels/personnel_list.html", context)


def single_personnel(request, personnel_id):
    single_personnel = get_object_or_404(Personnel, pk=personnel_id)
    context = {
        "single_personnel": single_personnel
    }
    return render(request, "personnels/single_personnel.html", context)


def create_personnel(request):
    if request.method == "POST":
        forms = PersonnelForm(request.POST, request.FILES or None)

        if forms.is_valid():
            forms.save()
        messages.success(request, "personnel Registration Successfully!")
        return redirect("personnel_list")
    else:
        forms = PersonnelForm()

    context = {
        "forms": forms
    }
    return render(request, "personnels/create_personnel.html", context)


def edit_personnel(request, pk):
    personnel_edit = Personnel.objects.get(id=pk)
    edit_personnel_forms = PersonnelForm(instance=personnel_edit)

    if request.method == "POST":
        edit_personnel_forms = PersonnelForm(request.POST, request.FILES or None, instance=personnel_edit)

        if edit_personnel_forms.is_valid():
            edit_personnel_forms.save()
            messages.success(request, "Edit personnel Info Successfully!")
            return redirect("personnel_list")

    context = {
        "edit_personnel_forms": edit_personnel_forms
    }
    return render(request, "personnels/edit_personnel.html", context)


def delete_personnel(request, personnel_id):
    personnel_delete = Personnel.objects.get(id=personnel_id)
    personnel_delete.delete()
    messages.success(request, "Delete personnel Info Successfully")
    return redirect("personnel_list")



    #payement
from django.shortcuts import render, get_object_or_404, redirect
from .models import Personnel, PaymentHistory
from .forms import PaymentForm

def add_payment(request, personnel_id):
    personnel = get_object_or_404(Personnel, pk=personnel_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.personnel = personnel
            payment.save()
            return redirect('personnel_detail', personnel_id=personnel.id)
    else:
        form = PaymentForm()
    return render(request, 'add_payment.html', {'form': form, 'personnel':personnel})

def edit_payment(request, payment_id):
    payment = get_object_or_404(PaymentHistory, pk=payment_id)
    personnel = payment.personnel
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('personnel_detail', personnel_id=personnel.id)
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'edit_payment.html', {'form': form, 'personnel': personnel})
