from django.shortcuts import render
from .models import *



def home(request):  
    request.session['user'] = ''
    return render(request, 'login.html')
# Create your views here.
def login(request):  
    if request.method == 'POST':
        data = request.POST.dict()
        if data['username'] == '' or data['password'] == '':
            return render(request,'login.html',context={'resposta':"Por favor, preencha todos os campos"})
        else:
            try:
                Usuarios.objects.get(nome=data['username'],senha=int(data['password']))
                request.session['user'] = data['username']
                receitas = Receitas.objects.filter(usuario=data['username']).all()
                return render(request,'home.html',context={'receitas':list(set(receitas))})
            except:
                return render(request,'login.html',context={'resposta':"Usuário não encontrado"})
    else:
        request.session['user'] = ''
        return render(request,'login.html')
    

def load_recipes(request):
    if request.method == 'POST':
        data = request.POST.dict()
        if data['data'] == '' and data['tipo']== '' and data['nome'] == '':
             receitas = Receitas.objects.filter(usuario=request.session.get('user')).all()
        else:
            if data['data'] != '':
                receitas = Receitas.objects.filter(data=data['data'],usuario=request.session.get('user')).all()
            elif data['nome']!= '':
                receitas = Receitas.objects.filter(nome=str(data['nome']),usuario=request.session.get('user')).all()
            elif data['tipo']!= '':
                receitas = Receitas.objects.filter(tipo=str(data['tipo']),usuario=request.session.get('user')).all()
        return render(request,'home.html',context={'receitas':receitas})
    else:
        return render(request,'home.html',context={"receitas":Receitas.objects.filter(usuario=request.session.get('user')).all()})

def delete_recipe(request):
    data= request.POST.dict()
    try:
        receita = Receitas.objects.get(id=int(data['id']),usuario=request.session.get('user'))
        receita.delete()
        Receitas.save()
        return render(request,'home.html',context={'receitas':Receitas.objects.filter(usuario=request.session.get('user')).all()})
    except:
        return render(request,'home.html',context={'resposta':"Erro"})
# Create your views here.

def load_new_recipes(request):
    return render(request,'nova_receita.html')

def new_recipe(request):
    usuario = request.session['user']
    if Usuarios.objects.filter(nome=usuario).exists():
        index = Receitas.objects.last().id
        dicionario = request.POST.dict()    
        nova_receita = Receitas(
            id = int(index)+1,
            nome=dicionario.get('nome'),
            usuario = usuario,
            infos = dicionario.get("infos"),
            data = dicionario.get('data'),
            tipo  = dicionario.get("tipos")
        )
        nova_receita.save()
        return render(request,'home.html',context={"receitas":Receitas.objects.filter(usuario=usuario).all()})
    else:
        return render(request,'home.hmtl',context={"resposta":"Erro ao criar uma nova receita"})
    
def see_recipe(request):
    usuario = request.session['user']
    if Usuarios.objects.filter(nome=usuario).exists():
        data = request.POST.dict()
        receita = Receitas.objects.get(id=int(data['id']),usuario=request.session.get('user')).infos
        return render(request,'ver_receita.html',{'receita':receita})
    else:
        return render(request,'home.html')

def profile(request):
    usuario = request.session['user']
    if Usuarios.objects.filter(nome=usuario).exists():
        user = Usuarios.objects.get(nome=usuario)
        dados = Receitas.objects.filter(usuario=user.nome).all()
        print(dados)
        return render(request,'perfil.html',{'infos':user,'dados':len(dados)})
    else:
        return render(request,'home.html')

def update_password(request):
    usuario = request.session['user']
    if Usuarios.objects.filter(nome=usuario).exists():
        data = request.POST.dict()
        Usuarios.objects.filter(nome=usuario).update(senha=int(data['senha']))
        return render(request,'login.html')
    else:
        return render(request,'perfil.html')

def delete_profile(request):
    usuario = request.session['user']
    if Usuarios.objects.filter(nome=usuario).exists():
        user = Usuarios.objects.filter(nome=usuario)
        user.delete()
        request.session['user'] = ''
        return render(request,'login.html')
    else:
        return render(request,'login.html')

