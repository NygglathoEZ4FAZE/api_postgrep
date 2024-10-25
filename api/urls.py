from django.urls import path
from .views import query_database, query_database_tabla, update_record, delete_record

urlpatterns = [
    path('consulta_intent/', query_database, name='consulta_intent'), 
    path('actulizar/', update_record, name='actulizar'), 
    path('eliminar/', delete_record, name='eliminar'), 
    path('obterner_registros/', query_database_tabla, name='obterner_registros'), 
]
