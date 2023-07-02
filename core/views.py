from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Inmueble, FotoInmueble, Cliente, CorredoraPropiedad, Region, Ciudad, Comuna



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






def registro_usuario(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        rut_cli = request.POST['rut_cli']
        dv_cli = request.POST['dv_cli']
        nombre_cli = request.POST['nombre_cli']
        apat_cli = request.POST['apat_cli']
        amat_cli = request.POST['amat_cli']
        dir_cli = request.POST['dir_cli']
        fecha_nac_cli = request.POST['fecha_nac_cli']
        email_cli = request.POST['correo']
        celular_cli = request.POST['telefono']
        contrasena_cli = request.POST['password']
        estado_suscripcion_cli = 'I'  # Valor predeterminado
        id_com = request.POST['id_com']
        

        # Crear un nuevo cliente
        cliente = Cliente(rut_cli=rut_cli, dv_cli=dv_cli, nombre_cli=nombre_cli, apat_cli=apat_cli,
                          amat_cli=amat_cli, dir_cli=dir_cli, fecha_nac_cli=fecha_nac_cli, email_cli=email_cli,
                          celular_cli=celular_cli, contrasena_cli=contrasena_cli,
                          estado_suscripcion_cli=estado_suscripcion_cli, id_com_id=id_com)
        cliente.save()

        # Redireccionar a una página de éxito o a donde desees después del registro
        return redirect('registro_exitoso')

    # Si el método es GET, renderiza el formulario vacío
    return render(request, 'registro.html')