# accounts/views.py

from django.shortcuts import render, redirect
from .models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                # Si las credenciales son correctas
                return redirect('home')  # Redirigir a la página de "Hola Mundo"
            else:
                error_message = "Credenciales incorrectas"
        except User.DoesNotExist:
            error_message = "Usuario no encontrado"
        
        return render(request, 'accounts/login.html', {'error_message': error_message})
    
    return render(request, 'accounts/login.html')

def home_view(request):
    return render(request, 'accounts/home.html')
