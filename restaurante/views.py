from django.shortcuts import render


def menu_list(request):
    return render(request, 'restaurante/menu_list.html', {})