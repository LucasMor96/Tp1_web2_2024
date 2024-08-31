from django.shortcuts import render, redirect
from .models import Mensaje


#Se define la vista para filtrar segun el destinatario

def mensajes_recibidos(request):
    # Filtrar solo si se escribió
    # 'barraBuscar' == nombre del formulario
    query = request.GET.get('barraBuscar')  
    if query:
        # Si encuentra filtrar msjs por destinatario
        print("Buscando mensajes con destinatario que contenga:", query)
        mensajes = Mensaje.objects.filter(destinatario__icontains=query)
        # Si no hay mensajes que coincidan con la búsqueda
        if not mensajes.exists():
            no_coincidencias = True
        else:
            no_coincidencias = False
    else:
        # Si no hay búsqueda, mostrar todos
        mensajes = Mensaje.objects.all()
        no_coincidencias = False
    # Si no hay mensajes y no se buscó nada
    if not mensajes.exists() and not query:
        mensajes = []

    #retornar la vista con los mensajes, y si no hay coincidencias
    return render(request, 'mensajes/mensajes_recibidos.html', {'mensajes': mensajes})


def pagina_inicio(request):
    return render(request, 'mensajes/inicio.html')

def enviar_mensaje(request):
    if request.method == 'POST':
        texto = request.POST['texto']
        remitente = request.POST['remitente']
        destinatario = request.POST['destinatario']

        # Crear el mensaje con el método create
        Mensaje.objects.create(
            texto=texto,
            remitente=remitente,
            destinatario=destinatario
        )
        print("Mensaje enviado")
        return redirect('mensajes_recibidos')
    return render(request, 'mensajes/enviar_mensaje.html')
#primera version de mensajes_recibidos
'''def mensajes_recibidos(request):
    destinatario = 'destinatariomensaje'
    mensajes= Mensaje.objects.filter(destinatario=destinatario)
    return render (request, 'mensajes/mensajes_recibidos.html', {'mensajes': mensajes})
'''