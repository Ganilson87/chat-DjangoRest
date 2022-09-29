from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class mensagem(models.Model):
    emissor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emissor')
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receptor')
    conteudo = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.conteudo

    class Meta: 
        ordering = ('timestamp',)