"""
URL configuration for broken_minds project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# Esta es tu primera "Vista". Recibe la petición del navegador y responde con HTML.
def home(request):
    return HttpResponse("""
        <style>
            body { font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #f0f2f5; margin: 0; }
            .card { text-align: center; background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
            h1 { color: #092e20; } /* El color verde clásico de Django */
        </style>
        <div class="card">
            <h1>Broken Minds</h1>
            <p>UN BALURDO INTENTO DE APOYO PSICOLOGICO</p>
        </div>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # La ruta vacía '' significa la página de inicio (http://127.0.0.1:8000/)
]