from django.urls import path
from core.views import home, page_casas, detalle_casa, page_deptos, detalle_depto, registro_usuario, login_view, mi_perfil
from django.shortcuts import render
from django.conf import settings 
from django.conf.urls.static import static



urlpatterns = [
    path('', home, name='home'),
    path('pageCasa.html', page_casas, name='page_casa'),
    path('pageDepartamento.html', page_deptos, name='page_departamento'),
    path('pageContacto.html', lambda request: render(request, 'core/pageContacto.html'), name='page_ccontacto'),
     path('home/', home, name='page_home'),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('pagina_exito.html', lambda request: render(request, 'core/pagina_exito.html'), name='pagina_exito'),       
    path('iniciarSesion.html', lambda request: render(request, 'core/IniciarSesion.html'), name='page_iniciarSesion'),
    path('pageNosotros.html', lambda request: render(request, 'core/pageNosotros.html'), name='page_nosotros'),
    path('detalleCasa/<int:inmueble_id>/', detalle_casa, name='detalle_casa'),
    path('detalleDepartamento/<int:inmueble_id>/', detalle_depto, name='detalle_depto'),

    path('login/', login_view, name='login'),
    path('perfil/', mi_perfil, name='mi_perfil'),

    
   

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
