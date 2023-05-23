from django.shortcuts import render, get_object_or_404, redirect
from .models import Article


from .forms import ArticleForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages

from django.conf import settings
from django.shortcuts import render
from django.views.generic import *
from django.shortcuts import get_object_or_404


from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib import messages
from django.core.mail import send_mail

from .forms import  DemandeProjetEditForm, DemandeProjetForm,DemandeProjetEditForm
from .models import Clients, DemandeProjet



from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#@user_passes_test(lambda u: u.is_superuser)#, login_url='/error/'



def article_list(request):
    articles = Article.objects.all()
    
    paginator = Paginator(articles, 1)
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)

    context = {
        "articles": paged_articles
    }
    return render(request, "blog/article_list.html", context)

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article_detail.html', {'article': article})

def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'blog/article_create.html', {'form': form})

def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/article_update.html', {'form': form, 'article': article})

def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'blog/article_delete.html', {'article': article})





#--------------------------------------------------DEMANDE PROJETS------------------------------------------------------------------

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
    return render(request, 'demande/demande_projet.html', {'form': form})

def demande_projet_list(request):
    demandes_projet = DemandeProjet.objects.all()
    return render(request, 'demande/demande_projet_list.html', {'demandes_projet': demandes_projet})


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
    return render(request, 'demande/modifier_demande_projet.html', {'form': form})

def supprimer_demande_projet(request, demande_projet_id):
    demande_projet = get_object_or_404(DemandeProjet, id=demande_projet_id)
    demande_projet.delete()
    return redirect('demande_projet_list')



    from django.shortcuts import render, redirect
from .forms import DemandeProjetForm

def demande_projet(request):
    if request.method == 'POST':
        form = DemandeProjetForm(request.POST)
        if form.is_valid():
            form.save()
            # Faites les actions nécessaires après la sauvegarde du projet
            return redirect('indexA')  # Redirige vers la page d'accueil après la soumission réussie
    else:
        form = DemandeProjetForm()
    
    context = {'form': form}
    return render(request, 'demande/demandeprojet.html', context)


    