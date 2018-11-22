from django.shortcuts import render  

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import menuForm, platoForm     
from .models import Menu, Plato
from django.contrib import messages

def menu_list(request):
    menus = Menu.objects.all()
    return render(request, 'restaurante/menu_list.html', {'menus': menus})

def menu_nuevo(request):
    if request.method == "POST":
        formulario = menuForm(request.POST)
        if formulario.is_valid():
            menu = menu.objects.create(nombre=formulario.cleaned_data['nombre'])
            for plato_id in request.POST.getlist('plato'):
                carta = Carta(plato_id=plato_id, menu_id = menu_id)
                carta.save()
            messages.add_message(request, messages.SUCCESS, 'menu Guardado Exitosamente')
            return redirect('menu_list')
    else:
        formulario = menuForm()
    return render(request, 'restaurante/agregar.html', {'formulario': formulario})