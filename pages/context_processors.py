# Importa el modelo 'Page' desde el módulo 'pages.models'
from pages.models import Page

# Define una función llamada 'get_pages' que toma una solicitud 'request' como argumento
def get_pages(request):
    # Utiliza el modelo 'Page' para consultar la base de datos y obtener ciertos campos de las páginas
    # Utiliza 'values_list' para seleccionar los campos 'id', 'title', y 'slug' de todas las páginas
    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug')

    # Devuelve un diccionario que contiene un elemento 'pages' con la lista de páginas obtenidas
    # Esto hace que los datos estén disponibles para su uso en las plantillas HTML
    return {
        'pages': pages
    }


