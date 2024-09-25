# Importa la clase 'models' desde el módulo 'django.db'
from django.db import models

# Importa el campo 'RichTextField' desde el módulo 'ckeditor.fields'
from ckeditor.fields import RichTextField

# Define un modelo llamado 'Page'
class Page(models.Model):
    # Campo 'title' para almacenar el título de la página con un límite máximo de 50 caracteres
    title = models.CharField(
        max_length=50,  # Establece el límite máximo de caracteres
        verbose_name="Título"  # Etiqueta legible para la interfaz administrativa
    )
    
    # Campo 'content' para almacenar el contenido de la página (texto largo)
    content = RichTextField(  # Utiliza RichTextField de CKEditor para contenido enriquecido
        verbose_name="Contenido"  # Etiqueta legible para la interfaz administrativa
    )
    
    # Campo 'slug' para almacenar una cadena única que identifica la página (URL amigable)
    slug = models.CharField(
        unique=True,  # Asegura que cada slug sea único
        max_length=150,  # Establece el límite máximo de caracteres
        verbose_name="URL amigable"  # Etiqueta legible para la interfaz administrativa
    )

    order = models.IntegerField(
        default=0,verbose_name="Orden" 
    )
    
    # Campo 'visible' para indicar si la página es visible o no (booleano)
    visible = models.BooleanField(
        verbose_name="Visible"  # Etiqueta legible para la interfaz administrativa
    )
    
    # Campo 'created_at' para registrar la fecha y hora de creación de la página (automático)
    created_at = models.DateTimeField(
        auto_now_add=True,  # Se establece automáticamente en la fecha y hora actual al crear
        verbose_name="Creado el"  # Etiqueta legible para la interfaz administrativa
    )
    
    # Campo 'updated_at' para registrar la fecha y hora de actualización de la página (automático)
    updated_at = models.DateTimeField(
        auto_now=True,  # Se actualiza automáticamente en la fecha y hora actual al guardar
        verbose_name="Actualizado el"  # Etiqueta legible para la interfaz administrativa
    )

    # Define la clase 'Meta' para configuraciones adicionales del modelo
    class Meta:
        # 'verbose_name' se utiliza para establecer un nombre legible en singular para el modelo en la interfaz administrativa
        verbose_name = "Página"
    
        # 'verbose_name_plural' se utiliza para establecer un nombre legible en plural para el modelo en la interfaz administrativa
        verbose_name_plural = "Páginas"

    # Define el método '__str__' para representar el modelo como una cadena de texto legible
    def __str__(self):
        # Devuelve el valor del campo 'title' como representación de cadena del modelo
        return self.title

