from django.contrib import admin
from .models import Menu, Plato, MenuAdmin, PlatoAdmin, Cliente, ClienteAdmin, Empleado, EmpleadoAdmin

admin.site.register(Menu, MenuAdmin)
admin.site.register(Plato, PlatoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
