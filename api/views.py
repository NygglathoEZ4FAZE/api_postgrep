import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SoporteN1

# Consulta en base a una intención
@csrf_exempt
def query_database(request, intent):
    if request.method == 'GET':
        try:
            # Realizar la consulta usando el ORM de Django
            results = SoporteN1.objects.filter(intent=intent).values('id', 'instruction', 'response')
            
            if not results:
                return JsonResponse({"message": f"No se encontraron resultados para el intent: {intent}"}, status=404)
            
            return JsonResponse(list(results), safe=False, status=200)

        except Exception as e:
            return JsonResponse({"error": f"Ocurrió un error al consultar la base de datos: {e}"}, status=500)

    return JsonResponse({'error': 'Método no permitido. Usa GET.'}, status=405)

# Consulta para obtener todos los datos de la tabla
@csrf_exempt
def query_database_tabla(request):
    if request.method == 'GET':
        try:
            # Consultar todos los registros de la tabla soporte_n1
            results = SoporteN1.objects.all().values()  # Obtiene todos los campos de la tabla
            
            return JsonResponse(list(results), safe=False, status=200)
        
        except Exception as e:
            return JsonResponse({"error": f"Ocurrió un error al consultar la base de datos: {e}"}, status=500)

    return JsonResponse({'error': 'Método no permitido. Usa GET.'}, status=405)

# Consulta para actualizar registros
@csrf_exempt
def update_record(request, record_id):
    if request.method == 'PUT':
        try:
            # Buscar el registro por su id
            record = SoporteN1.objects.get(id=record_id)
            
            # Obtener los datos del cuerpo de la solicitud
            data = json.loads(request.body)
            instruction = data.get('instruction')
            category = data.get('category')
            intent = data.get('intent')
            response = data.get('response')
            date = data.get('date')
            
            # Actualizar los campos
            record.instruction = instruction
            record.categoria = category
            record.intent = intent
            record.response = response
            record.date = date
            
            # Guardar los cambios en la base de datos
            record.save()
            
            return JsonResponse({"message": f"El registro con ID {record_id} fue actualizado exitosamente."}, status=200)
        
        except SoporteN1.DoesNotExist:
            return JsonResponse({"error": f"No se encontró el registro con ID {record_id}."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Ocurrió un error al actualizar el registro: {e}"}, status=500)

    return JsonResponse({'error': 'Método no permitido. Usa PUT.'}, status=405)

@csrf_exempt
def delete_record(request, record_id):
    if request.method == 'DELETE':
        try:
            # Buscar el registro por su ID
            record = SoporteN1.objects.get(id=record_id)
            # Eliminar el registro de la base de datos
            record.delete()
            return JsonResponse({"message": f"El registro con ID {record_id} fue eliminado exitosamente."}, status=200)

        except SoporteN1.DoesNotExist:
            return JsonResponse({"error": f"No se encontró el registro con ID {record_id}."}, status=404)
        except Exception as e:
            return JsonResponse({"error": f"Ocurrió un error al eliminar el registro: {e}"}, status=500)

    return JsonResponse({'error': 'Método no permitido. Usa DELETE.'}, status=405)
