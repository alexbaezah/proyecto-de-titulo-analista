from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Inmueble, FotoInmueble, Cliente
from django.contrib import messages
from django.views.generic import ListView




# Create your views here.

def home(request):
    inmuebles = Inmueble.objects.all()

    casas = Inmueble.objects.filter(tipo_inmueble="Casa")
    departamentos = Inmueble.objects.filter(tipo_inmueble="Departamento")

    context = {
        "nombre": "Connito",
        "casas": casas,
        "departamentos": departamentos,
    }
    print(casas)
    print(departamentos)
    return render(request, 'core/home.html', context)




def page_casas(request):
    casas = Inmueble.objects.filter(tipo_inmueble="Casa")
    
    context = {
        'casas': casas
    }

    

    return render(request, 'core/pageCasa.html', context)


def detalle_casa(request, inmueble_id):
    try:
        # Obtener el inmueble por su ID
        inmueble = Inmueble.objects.get(id_inmb=inmueble_id)

        # Verificar si el inmueble es una casa (tipo_inmb = 1)
        if inmueble.tipo_inmueble == "Casa":
            # Resto del código para obtener los datos del propietario y el estado del inmueble

            # Obtener el propietario
            propietario = inmueble.rut_cli

            # Obtener el estado del inmueble
            estado = inmueble.estado_inmueble

            # Obtener comuna
            comuna = inmueble.comuna_inmb

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
    except Inmueble.DoesNotExist:
        # Si el inmueble no existe, puedes mostrar un mensaje de error o redirigir a otra página
        return HttpResponse("El inmueble no existe")


#Acá está lo relacionado a deptos

def page_deptos(request):
    departamentos = Inmueble.objects.filter(tipo_inmueble="Departamento")

    context = {
        'deptos': departamentos
    }


    return render(request, 'core/pageDepartamento.html', context)


def detalle_depto(request, inmueble_id):

    try: 
        inmueble = Inmueble.objects.get(id_inmb=inmueble_id)
    
    
        if inmueble.tipo_inmueble == "Departamento":
            # Resto del código para obtener los datos del propietario y el estado del inmueble
            
            # Obtener el propietario
            propietario = inmueble.rut_cli
            
            # Obtener el estado del inmueble
            estado = inmueble.estado_inmueble

            # Obtener comuna 
            comuna = inmueble.comuna_inmb

            # Renderizar el template con los datos
            return render(request, 'detalleDepartamento.html', {
                'depto': inmueble,
                'propietario': propietario,
                'estado': estado,
                'comuna': comuna,
            })
        else:
            # Si el inmueble no es una casa, puedes mostrar un mensaje de error o redirigir a otra página
            return HttpResponse("El inmueble no es una casa")
    except Inmueble.DoesNotExist:
        # Si el inmueble no existe, puedes mostrar un mensaje de error o redirigir a otra página
        return HttpResponse("El inmueble no existe")



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
        email_cli = request.POST['email_cli']
        celular_cli = request.POST['celular_cli']
        contrasena_cli = request.POST['password']
        estado_suscripcion_cli = 'I'  # Valor predeterminado
        comuna_cli = request.POST['nombre_comuna']
        

        # Crear un nuevo cliente
        cliente = Cliente(rut_cli=rut_cli, dv_cli=dv_cli, nombre_cli=nombre_cli, apat_cli=apat_cli,
                          amat_cli=amat_cli, dir_cli=dir_cli, fecha_nac_cli=fecha_nac_cli, email_cli=email_cli,
                          celular_cli=celular_cli, contrasena_cli=contrasena_cli,
                          estado_suscripcion_cli=estado_suscripcion_cli, comuna_cli=comuna_cli)
        cliente.save()

        # Redireccionar a una página de éxito o a donde desees después del registro
        return redirect('registro_exitoso')
    else:
        comunas = [    (1, 'Las Condes'),    (2, 'Providencia'),    (3, 'Santiago'),    (4, 'Ñuñoa'),    (5, 'Vitacura'),    (6, 'La Reina'),    (7, 'La Florida'),    (8, 'Maipú'),    (9, 'Lo Barnechea'),    (10, 'Macul'),    (11, 'San Miguel'),    (12, 'Peñalolén'),    (13, 'Puente Alto'),    (14, 'Recoleta'),    (15, 'Estación Central'),    (16, 'San Bernardo'),    (17, 'Independencia'),    (18, 'La Cisterna'),    (19, 'Quilicura'),    (20, 'Quinta Normal'),    (21, 'Conchalí'),    (22, 'San Joaquín'),    (23, 'Huechuraba'),    (24, 'El Bosque'),    (25, 'Cerrillos'),    (26, 'Cerro Navia'),    (27, 'La Granja'),    (28, 'La Pintana'),    (29, 'Lo Espejo'),    (30, 'Lo Prado'),    (31, 'Pedro Aguirre Cerda'),    (32, 'Pudahuel'),    (33, 'Renca'),    (34, 'San Ramón'),    (35, 'Melipilla'),    (36, 'San Pedro'),    (37, 'Alhué'),    (38, 'María Pinto'),    (39, 'Curacaví'),    (40, 'Talagante'),    (41, 'El Monte'),    (42, 'Paine'),    (43, 'Peñaflor'),    (44, 'Isla de Maipo'),    (45, 'Colina'),    (46, 'Pirque')]



    # Si el método es GET, renderiza el formulario vacío
    return render(request, 'core/registro.html', {'comunas': comunas})


def open_session(request, email):
    # Verificar si el usuario ya tiene una sesión abierta
    if 'session_email' in request.session:
        # Si ya existe una sesión abierta, cerrarla antes de abrir una nueva
        close_session(request)
    
    # Establecer el correo electrónico del usuario en la sesión
    request.session['session_email'] = email

def close_session(request):
    # Eliminar el correo electrónico de la sesión
    if 'session_email' in request.session:
        del request.session['session_email']


def login_view(request):
    if request.method == 'POST':
        email = request.POST['usuario']
        password = request.POST['password']
        
        # Realizar la búsqueda en la base de datos para verificar las credenciales
        try:
            cliente = Cliente.objects.get(email_cli=email, contrasena_cli=password)
        except Cliente.DoesNotExist:
            cliente = None
        
        if cliente is not None:
            # Usuario autenticado, abrir sesión
            open_session(request, email)
            messages.success(request, 'Usuario autenticado')
            return render(request, 'core/login.html')
        else:
            # Usuario no autenticado, mostrar mensaje de error
            messages.error(request, 'Credenciales incorrectas')
            return render(request, 'core/login.html')
    else:
        return render(request, 'core/login.html')