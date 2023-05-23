from django.shortcuts import render
from students.models import Attendance
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ResultInfoSerializer, StudentInfoSerializer
from .models import Result
from students.models import StudentInfo
from .models import Equipe
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .forms import EquipForm
from django.contrib import messages

# Create your views here.
@api_view()
def student_attendance(request, student_class, student_id):
    try:
        Attendance.objects.create_attendance(student_class, student_id)
        return Response({"Status": "Atendance Counted Successfully"}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({"Status": "Attendance already has taken"}, status=status.HTTP_400_BAD_REQUEST)


# Class Based View (CBV)
class StudentAttendance(APIView):
    def get(self, request, student_class, student_id):
        try:
            Attendance.objects.create_attendance(student_class, student_id)
            return Response({"Status": "Atendance Counted Successfully"}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response({"Status": "Attendance already has taken"}, status=status.HTTP_400_BAD_REQUEST)


class ResultInfo(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        result_serializer = ResultInfoSerializer(data=request.data)
        if result_serializer.is_valid():
            board = result_serializer.validated_data["board"]
            roll = result_serializer.validated_data["roll"]
            result_obj = Result.objects.get(board=board, roll=roll)
            return Response({"Result": result_obj.gpa})

        return Response(result_serializer.errors)


class CreateStudentInfo(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        create_student_serializer = StudentInfoSerializer(data=request.data)
        if create_student_serializer.is_valid():
            create_student_serializer.save()
            return Response({"Status": "Success"}, status=status.HTTP_200_OK)
        else:
            return Response({"Status": create_student_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


#equipeeeee


def equipe_list(request):
    equipes = Equipe.objects.all()
    paginator = Paginator(equipes, 1)
    page = request.GET.get('page')
    paged_equipes = paginator.get_page(page)

    context = {
        "equipes": paged_equipes
    }
    return render(request, "equipes/equipe_list.html", context)


def create_equipe(request):
    if request.method == "POST":
        forms = EquipForm(request.POST, request.FILES or None)

        if forms.is_valid():
            forms.save()
        messages.success(request, "equipe Registration Successfully!")
        return redirect("equipe_list")
    else:
        forms = EquipForm()

    context = {
        "forms": forms
    }
    return render(request, "equipes/create_equipe.html", context)


def edit_equipe(request, pk):
    equipe = get_object_or_404(Equipe, pk=pk)
    if request.method == 'POST':
        form = EquipForm(request.POST, instance=equipe)
        if form.is_valid():
            equipe.save()
            return redirect('equipe_list')
    else:
        form = EquipForm(instance=equipe)
        return render(request, 'equipes/edit_equipe.html', {'form': form})

def delete_equipe(request, equipe_id):
    equipe_delete = Equipe.objects.get(id=equipe_id)
    equipe_delete.delete()
    messages.success(request, "Delete equipe Info Successfully")
    return redirect("equipe_list")




def detail_equipe(request, equipe_id):
    detail_equipe = get_object_or_404(Equipe, pk=equipe_id)
    context = {
        "detail_equipe": detail_equipe
    }
    return render(request, 'equipes/equipe_details.html', context)








