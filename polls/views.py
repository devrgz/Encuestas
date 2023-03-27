from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

"""
Estamos usando dos vistas genéricas aquí: ListView y DetailView. 
Respectivamente, esos dos vistas resumen los conceptos de “ muestran una lista de objetos ” y “ 
muestra una página de detalles para un tipo particular de objeto. ”
"""

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    
   


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        """
        request.POST es como un diccionario objeto que le permite acceder a los datos enviados por
        nombre de clave. En este caso, request.POST['choice'] devuelve la ID de la opción seleccionada, 
        como cuerda. request.POST los valores son siempre cuerdas.
        """
        
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))




"""

Estas vistas representan un caso común de desarrollo web básico: obtener datos de la base de datos de acuerdo con un parámetro pasado en la URL, 
cargando una plantilla y devolviendo la plantilla renderizada. Debido a que esto es tan común, 
Django proporciona un atajo, llamado sistema de vistas genéricas “ ”.

Una vista es un tipo “ ” de página web en su aplicación Django que generalmente sirve una función específica 
y tiene una plantilla específica.


Para pasar de una URL a una vista, Django usa lo que se conoce como ‘ URLconfs ’. A URLconf asigna patrones de URL a vistas.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


los render() la función toma el objeto de solicitud como su primer argumento, un nombre de plantilla como segundo argumento y un diccionario como tercer argumento opcional. 
Devuelve un HttpResponse objeto de la plantilla dada renderizada con el contexto dado.


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        
        request.POST es como un diccionario objeto que le permite acceder a los datos enviados por
        nombre de clave. En este caso, request.POST['choice'] devuelve la ID de la opción seleccionada, 
        como cuerda. request.POST los valores son siempre cuerdas.
        
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    
    Después de incrementar el recuento de opciones, el código devuelve un 
    HttpResponseRedirect en lugar de una normalidad HttpResponse. HttpResponseRedirect toma un solo argumento: el URL a la que se redirigirá al usuario
    
    Estamos usando el reverse() función en el HttpResponseRedirect 
    constructor en este ejemplo. Esta función ayuda a evitar tener que codificar una URL en la función de vista. 
    Se le da el nombre de la vista a la que queremos pasar el control y el porción variable del patrón URL que apunta a esa vista
    

    """