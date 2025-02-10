from django.shortcuts import render
from .models import *



def home(request):  
    request.session['user'] = ''
    return render(request, 'login.html')
# Create your views here.
def login(request):  
    data = request.POST.dict()
    print(data)
    if data['username'] == '' or data['password'] == '':
        return render(request,'login.html',context={'resposta':"Por favor, preencha todos os campos"})
    else:
        try:
            Usuarios.objects.get(nome=data['username'],senha=int(data['password']))
            request.session['user'] = data['username']
            return render(request,'home.html',context={'receitas':Receitas.objects.filter(usuario=data['username']).all()})
        except:
            return render(request,'login.html',context={'resposta':"Usuário não encontrado"})

def load_recipes(request):
        data = request.POST.dict()
        if data['data'] == '' and data['tipo']== '' and data['nome'] == '':
             receitas = Receitas.objects.filter(usuario=request.session.get('user')).all()
        else:
            if data['data'] != '':
                receitas = Receitas.objects.filter(data=data['data'],usuario=request.session.get('user')).all()
            elif data['nome']!= '':
                receitas = Receitas.objects.filter(nome=str(data['nome'],usuario=request.session.get('user'))).all()
            elif data['tipo']!= '':
                receitas = Receitas.objects.filter(tipo=str(data['tipo'],usuario=request.session.get('user'))).all()
        return render(request,'home.html',context={'receitas':receitas})

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
