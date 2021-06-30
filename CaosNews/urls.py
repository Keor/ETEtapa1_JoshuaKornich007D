from django.urls import path
from .views import home, colaboradores, new_colaborador, mod_colaborador, del_colaborador

urlpatterns = [
    path('',home,name="home"),
    path('colaboradores',colaboradores,name="colaboradores"),
    path('new_colaborador',new_colaborador,name="new_colaborador"),
    path('mod_colaborador/<id>', mod_colaborador, name="mod_colaborador"),
    path('del_colaborador/<id>', del_colaborador, name="del_colaborador"),

]