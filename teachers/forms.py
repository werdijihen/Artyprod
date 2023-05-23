from django import forms
from .models import TeacherInfo
from .models import Personnel
from .models import PaymentHistory
class CreateTeacher(forms.ModelForm):
    class Meta:
        model = TeacherInfo
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: John Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ex: john@gmail.com'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 30'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'teacher_img': forms.FileInput(attrs={'class': 'form-control'}),
            'passing_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2018-2020'}),
            'joining_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2018-12-31'}),
            'admission_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: LM01'}),
            'dept_type': forms.Select(attrs={'class': 'form-control'}),
            'sub_type': forms.Select(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 45000'}),
        }


class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields ="__all__"


class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentHistory
        fields = ['payment_date', 'payment_amount']
        widgets = {
            'payment_date': forms.DateInput(attrs={'class': 'datepicker'}),
        }