from django.shortcuts import render

def inicio(request):
    temas = [
        {
            'nombre': 'Seguridad en Redes',
            'descripcion': 'Configuración de VLANs y prevención de ataques.',
            'imagenes': ['css/js/images/tema1_1.png', 'css/js/images/tema1_2.png']
        },
        {
            'nombre': 'Desarrollo de Software Seguros',
            'descripcion': 'Prácticas de código limpio y mitigación de vulnerabilidades.',
            'imagenes': ['css/js/images/tema2_1.png', 'css/js/images/tema2_2.png']
        }
    ]
    return render(request, 'inicio_monteleone_venegas/inicio.html', {'lista_elementos': temas})