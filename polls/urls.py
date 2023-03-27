from django.urls import path
from . import views


app_name = 'polls' # ¿Cómo se hace uno haga que Django sepa qué vista de aplicación crear para una URL cuando use el etiqueta de plantilla?{% url %}
#La respuesta es agregar espacios de nombres a su URLconf. En el polls/urls.py archivo, adelante y agrega un app_name para establecer el espacio de nombres de la aplicación
urlpatterns = [
   path('', views.IndexView.as_view(), name='index'),
   path('<int:pk>/', views.DetailView.as_view(), name='detail'),
   path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
   path('<int:question_id>/vote/', views.vote, name='vote'),
]

"""
    os question_id=34 parte viene de <int:question_id>. Usando ángulo paréntesis “ captura ” parte de la URL y la envía 
    como argumento de palabra clave a la Ver función. los question_id parte de la cadena define el nombre que se utilizará 
    para identificar el patrón coincidente, y el int parte es un convertidor que determina qué patrones deben coincidir con esta 
    parte de la ruta URL. El colon (:) separa el convertidor y el nombre del patrón.
"""