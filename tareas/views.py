from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt # Herramienta temporal de seguridad
from .models import Tarea

@csrf_exempt # Esto evita problemas de seguridad por ahora, ya que no estamos usando archivos HTML externos
def lista_tareas(request):
    
    # 1. SI EL USUARIO ENVÍA EL FORMULARIO (PETICIÓN POST)
    if request.method == 'POST':
        texto_tarea = request.POST.get('titulo_tarea') # Captura lo que el usuario escribió en el input
        if texto_tarea:
            Tarea.objects.create(titulo=texto_tarea) # El ORM crea y guarda la tarea en la base de datos
        return redirect('/') # Redirecciona a la misma página para limpiar el formulario y ver los cambios

    # 2. SI EL USUARIO SOLO ENTRA A LA PÁGINA (PETICIÓN GET)
    tareas = Tarea.objects.all().order_by('-creada_en') # Trae las tareas, las más nuevas primero
    
    html_contenido = """
    <style>
        body { font-family: sans-serif; max-width: 600px; margin: 40px auto; padding: 20px; background-color: #f9f9f9; }
        h1 { color: #092e20; border-bottom: 2px solid #092e20; padding-bottom: 10px; }
        ul { list-style: none; padding: 0; }
        li { background: white; margin: 10px 0; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); display: flex; justify-content: space-between; }
        .completada { text-decoration: line-through; color: #888; }
        .pendiente { font-weight: bold; color: #333; }
        
        /* Estilos para el formulario */
        form { display: flex; gap: 10px; margin-bottom: 20px; }
        input[type="text"] { flex: 1; padding: 12px; border: 1px solid #ccc; border-radius: 6px; font-size: 16px; }
        button { background-color: #092e20; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-size: 16px; font-weight: bold; }
        button:hover { background-color: #134e35; }
    </style>
    
    <h1>🧠 Broken Minds - Lista de Tareas</h1>
    
    <form method="POST">
        <input type="text" name="titulo_tarea" placeholder="¿Qué tienes pendiente por hacer?" required>
        <button type="submit">Agregar</button>
    </form>
    
    <ul>
    """
    
    for tarea in tareas:
        clase = "completada" if tarea.completada else "pendiente"
        icono = "✅" if tarea.completada else "⏳"
        html_contenido += f"<li class='{clase}'><span>{icono} {tarea.titulo}</span></li>"
        
    html_contenido += "</ul>"
    
    return HttpResponse(html_contenido)