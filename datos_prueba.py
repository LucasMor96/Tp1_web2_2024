# datos_prueba.py
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TableroMensajes.settings')
django.setup()

from mensajes.models import Mensaje

# Crear datos de prueba
Mensaje.objects.create(
    texto='Hola, ¿cómo estás?',
    remitente='Juan',
    destinatario='Pedro',
    fecha_envio='2024-08-27 14:30:00'
)

Mensaje.objects.create(
    texto='¡Feliz cumpleaños!',
    remitente='Ana',
    destinatario='Carlos',
    fecha_envio='2024-08-27 10:00:00'
)

print('Datos de prueba agregados correctamente.')

