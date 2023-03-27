from django.contrib import admin
from django.urls import include, path

"""
os path() la función se pasa cuatro argumentos, 
se requieren dos: route y view, y dos opcionales: kwargs, y name.
En este punto, vale la pena revisar para qué son estos argumentos.
"""

"""
Django determina el módulo raíz URLconf para usar. Normalmente, este es el valor de la ROOT_URLCONF configuración, pero si la entrada HttpRequest el objeto tiene un urlconf atributo ( establecido por middleware ), su valor se utilizará en lugar de ROOT_URLCONF ajuste.
Django carga ese módulo Python y busca la variable urlpatterns. Esto debería ser un secuencia de django.urls.path() y / o django.urls.re_path() instancias.
Django ejecuta cada patrón de URL, en orden, y se detiene al principio uno que coincida con la URL solicitada, coincidente con path_info.
Una vez que uno de los patrones de URL coincide, Django importa y llama a lo dado vista, que es una función de Python ( o una vista basada en clases). La vista pasa lo siguiente argumentos:
Una instancia de HttpRequest.
Si el patrón de URL coincidente no contenía grupos con nombre, entonces el las coincidencias de la expresión regular se proporcionan como argumentos posicionales.
Los argumentos de las palabras clave están formados por cualquier parte nombrada que coincida con el expresión de ruta que se proporciona, anulada por cualquier argumento especificado en el opcional kwargs argumento a django.urls.path() o django.urls.re_path().
Si no hay un patrón de URL coincidente, o si se genera una excepción durante cualquier punto en este proceso, Django invoca un apropiado vista de manejo de errores. Ver Manejo de errores abajo.
"""
urlpatterns = [
    path('polls/', include('polls.urls')), #
    path('admin/', admin.site.urls),
]