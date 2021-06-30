from django.shortcuts import render,redirect,get_object_or_404
from .models import Colaborador
from .forms import ColaboradorForm

def home (request):

    return render (request,'home.html')

def colaboradores (request):
    colaboradores=Colaborador.objects.all()
    return render (request,'CaosNews/colaboradores.html',context={'colaboradores':colaboradores})

def new_colaborador(request):
    if request.method =='POST': 
        colaborador_new=ColaboradorForm(request.POST,request.FILES)
        contrapre=request.POST['rut'][:2]+request.POST['nomCompleto'][:2].upper()+request.POST['pais'][-2:]+request.POST['fono'][-2:]
        colaborador_new.data=colaborador_new.data.copy()
        colaborador_new.data['contrasena']=contrapre
        if colaborador_new.is_valid():
            colaborador_new.save()
            return redirect('home')
    else: 
        colaborador_new=ColaboradorForm()
    return render(request, 'CaosNews/new_colaborador.html', {'colaborador_new': colaborador_new})

def mod_colaborador(request,id):
    colaborador = get_object_or_404(Colaborador,rut=id)
    datos ={'form': ColaboradorForm(instance=colaborador)}
    if request.method == 'POST':
        formulario = ColaboradorForm(request.POST, request.FILES, instance = colaborador)
        if formulario.is_valid():
            formulario.save()
            return redirect('colaboradores')
    return render(request, 'CaosNews/mod_colaborador.html', datos)

def del_colaborador(request,id):
    colaborador = get_object_or_404(Colaborador,rut=id)
    colaborador.delete()
    return redirect('colaboradores')