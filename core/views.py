from django.shortcuts import render
from django.http import HttpResponse
from .models import Inmueble, FotoInmueble, Cliente, CorredoraPropiedad

# Create your views here.

def home(request):
    departamentos = Inmueble.objects.filter(id_tipo_inmb=2)[:8]  # Filtrar y obtener máximo 8 departamentos
    casas = Inmueble.objects.filter(id_tipo_inmb=1)[:8]  # Filtrar y obtener máximo 8 casas
    listaColor = ['negro','gris azulado','3 leche']
    context = { "nombre": "Connito", "listaColor": listaColor, 
                'departamentos': departamentos, 
                'casas': casas,               
               }
    
    return render(request, 'core/home.html', context)

    


def page_departamentos(request):
    departamentos = Inmueble.objects.filter(id_tipo_inmb=2)  # Filtrar los departamentos (id_tipo_inmb=2)

    context = {
        'departamentos': departamentos
    }

    return render(request, 'core/pageDepartamento.html', context)

# acá está lo relacioando a casas


def page_casas(request):
    casas = Inmueble.objects.filter(id_tipo_inmb=1)  # Filtrar las casas (id_tipo_inmb=1)

    context = {
        'casas': casas
    }

    for casa in casas:
        fotos = FotoInmueble.objects.filter(id_inmb=casa.id_inmb)
        casa.fotos = fotos

    return render(request, 'core/pageCasa.html', context)



def detalle_casa(request, inmueble_id):
    # Obtener el inmueble
    inmueble = Inmueble.objects.get(id_inmb=inmueble_id)

    # Verificar si el inmueble es una casa (tipo_inmb = 1)
    if inmueble.id_tipo_inmb.id_tipo_inmb == 1:
        # Resto del código para obtener los datos del propietario y el estado del inmueble
        
        # Obtener el propietario
        propietario = inmueble.rut_cli
        
        # Obtener el estado del inmueble
        estado = inmueble.cod_estado_inmb

        # Obtener comuna 
        comuna = inmueble.id_com



        # Renderizar el template con los datos
        return render(request, 'detalleCasa.html', {
            'casa': inmueble,
            'propietario': propietario,
            'estado': estado,
            'comuna': comuna,
        })
    else:
        # Si el inmueble no es una casa, puedes mostrar un mensaje de error o redirigir a otra página
        return HttpResponse("El inmueble no es una casa")


#Acá está lo relacionado a deptos

def page_deptos(request):
    deptos = Inmueble.objects.filter(id_tipo_inmb=2)  # Filtrar los deptos (id_tipo_inmb=2)

    context = {
        'deptos': deptos
    }


    return render(request, 'core/pageDepartamento.html', context)


def detalle_depto(request, inmueble_id):
    # Obtener el inmueble
    inmueble = Inmueble.objects.get(id_inmb=inmueble_id)

    # Verificar si el inmueble es un depto (tipo_inmb = 2)
    if inmueble.id_tipo_inmb.id_tipo_inmb == 2:
        # Resto del código para obtener los datos del propietario y el estado del inmueble
        
        # Obtener el propietario
        propietario = inmueble.rut_cli
        
        # Obtener el estado del inmueble
        estado = inmueble.cod_estado_inmb

        # Obtener comuna 
        comuna = inmueble.id_com

        # Renderizar el template con los datos
        return render(request, 'detalleDepartamento.html', {
            'depto': inmueble,
            'propietario': propietario,
            'estado': estado,
            'comuna': comuna,
        })
    else:
        # Si el inmueble no es una casa, puedes mostrar un mensaje de error o redirigir a otra página
        return HttpResponse("El inmueble no es un departamento")


#127.0.0.1:8000/ 