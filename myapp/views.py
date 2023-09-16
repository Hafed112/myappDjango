from django.shortcuts import render,redirect
from .forms import StagiaireFroms
from .models import Stagiaire
# Create your views here.

def stagiaire_form(request,id=0):
    if request.method =="GET":
        if id==0:
            form=StagiaireFroms()
        else:
            stg=Stagiaire.objects.get(pk=id)
            form=StagiaireFroms(instance=stg)
        return render(request,"stagiaire_myapp/stgForm.html",{'form':form})
    else:
        if id==0:
            form=StagiaireFroms(request.POST)
        else:
            stg=Stagiaire.objects.get(pk=id)
            form=StagiaireFroms(request.POST,instance=stg)
        if (form.is_valid):
            form.save()
    return redirect('/list')

def stagiaire_list(request):
    data={'stgData':Stagiaire.objects.all()}
    return render(request,"stagiaire_myapp/listStg.html",data)

def stagiaire_delete(request,id):
    stg=Stagiaire.objects.get(pk=id)
    stg.delete()
    return redirect('/list')