from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_filter = ['pub_date'] # AÑade un filtro de busqueda 
    #El tipo de filtro que se muestra depende del tipo de campo en el que se está filtrando. Porque pub_date es un DateTimeField, Django sabe dar opciones de filtro apropiadas: “ Cualquier fecha ”, “ Hoy ”, “ Pasado 7 días ”, “ Este mes ”, “ Este año ”.
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently') # Variable para que al modificar, se muestren el nombre y los datos de las tablas
    search_fields = ['question_text']

"""Esto le dice a Django: “Choice los objetos se editan en el Question página de administración. 
Por predeterminado, proporcione suficientes campos para 3 opciones. ”"""

admin.site.register(Question, QuestionAdmin)
