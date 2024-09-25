# Importa la clase 'admin' desde el módulo 'django.contrib'
from django.contrib import admin

# Importa el modelo 'Page' desde el archivo '.models' en el mismo directorio
from .models import Page  

#configuracion extra 
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    search_fields = ('title','content')
    list_filter = ('visible',)
    list_display = ('title','visible','created_at')
    ordering = ('created_at',)

# Registra el modelo 'Page' en el panel de administración de Django
admin.site.register(Page, PageAdmin)

# Define variables para personalizar la apariencia del panel de administración
title = "Proyecto con Django"  # Título principal del panel de administración
subtitle = "Panel de Gestión"    # Subtítulo del panel de administración

# Personaliza el encabezado del sitio en el panel de administración
admin.site.site_header = title

# Personaliza el título en la pestaña del navegador para el panel de administración
admin.site.site_title = title

# Personaliza el título en la página principal del panel de administración
admin.site.index_title = subtitle
