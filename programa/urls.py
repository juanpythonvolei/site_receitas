"""
URL configuration for programa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from site_receitas.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/',login,name='login'),
    path('home/filtros/',load_recipes,name='load_recipes'),
    path('home/delecao/',delete_recipe,name='apagar_receita'),
    path('home/adicao/',load_new_recipes,name='nova_receita_page'),
    path('home/adicao/acao/',new_recipe,name='nova_receita'),
    path('home/visualizacao/',see_recipe,name='ver_receita'),
    path('home/perfil/',profile,name='perfil'),
    path('home/perfil/alteracaosenha/',update_password,name='mudar_senha'),
    path('home/perfil/exclusao/',delete_profile,name='apagar_perfil')
]
