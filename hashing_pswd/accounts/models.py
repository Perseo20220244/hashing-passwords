# accounts/models.py

from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # La contraseña será "hasheada"

    def set_password(self, raw_password):
        #Método para hashear la contraseña manualmente
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        #Verificar la contraseña contra el valor hasheado
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return self.username
