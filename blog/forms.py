from django import forms
from blog.models import Article,DemandeProjet
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields ="__all__" 
        
        
class ClientCreationForm(UserCreationForm):
    nom = forms.CharField(max_length=255)
    adresse = forms.CharField(max_length=255)
    telephone = forms.CharField(max_length=255)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'nom', 'adresse', 'telephone', 'email']
class DemandeProjetForm(forms.ModelForm):
    class Meta:
        model = DemandeProjet
        fields ="__all__"  

class DemandeProjetEditForm(forms.ModelForm):
    class Meta:
        model = DemandeProjet
        fields ="__all__" 
