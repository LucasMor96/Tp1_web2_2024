from django.db import models

# Modelos con los que trabaja la app de mensajes
class Mensaje(models.Model):
    texto = models.TextField()
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.remitente} a {self.destinatario}: {self.texto[:50]}'

