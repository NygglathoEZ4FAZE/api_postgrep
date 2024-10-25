from django.db import models

class SoporteN1(models.Model):
    instruction = models.TextField(db_column='instruction')  # Usa db_column si el nombre en la base de datos es diferente
    categoria = models.TextField(db_column='category')  # Asegúrate de que los nombres de los campos coincidan
    intent = models.TextField(db_column='intent')
    response = models.TextField(db_column='response')
    date = models.TextField(db_column='date')

    class Meta:
        db_table = 'soporte_n1'  # Aquí especificas el nombre exacto de la tabla en la base de datos
        managed = False  # Indica que Django no debe gestionar la creación/actualización de esta tabla