from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    nombre_reg = models.CharField(max_length=80)


class Ciudad(models.Model):
    id_ciudad = models.IntegerField(primary_key=True)
    nom_ciud = models.CharField(max_length=80)
    id_region = models.ForeignKey('Region', on_delete=models.CASCADE, db_column='ID_REGION')

class Comuna(models.Model):
    id_com = models.AutoField(primary_key=True)
    nom_com = models.CharField(max_length=100)
    id_ciudad = models.ForeignKey('Ciudad', on_delete=models.CASCADE, db_column='ID_CIUDAD')
    

    def __str__(self):
        return self.nom_com
    
    class Meta:
        db_table = 'COMUNA'

class Cliente(models.Model):
    rut_cli = models.CharField(max_length=8, primary_key=True)
    dv_cli = models.CharField(max_length=1)
    nombre_cli = models.CharField(max_length=80)
    apat_cli = models.CharField(max_length=80)
    amat_cli = models.CharField(max_length=80)
    dir_cli = models.CharField(max_length=100)
    fecha_nac_cli = models.DateField()
    email_cli = models.EmailField()
    celular_cli = models.CharField(max_length=12)
    contrasena_cli = models.CharField(max_length=6)
    estado_suscripcion_cli = models.CharField(max_length=1, default='I')
    comuna_cli = models.CharField(max_length=100)
    

    class Meta:
        db_table = 'CLIENTE'


class CorredoraPropiedad(models.Model):
    rut_corr = models.CharField(max_length=8, primary_key=True)
    dv_corr = models.CharField(max_length=1)
    nombre_corr = models.CharField(max_length=100)
    dir_corr = models.CharField(max_length=100)
    telefono_corr = models.CharField(max_length=12)
    email_corr = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=6)
    sitio_web_corr = models.CharField(max_length=100, null=True, blank=True)
    estado_suscripcion_corr = models.CharField(max_length=1, default='I')
    id_com = models.ForeignKey('Comuna', on_delete=models.CASCADE)
    id_suscr = models.ForeignKey('Suscripcion', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_corr

    class Meta:
        db_table = 'CORREDORA_PROPIEDAD'

class TipoSuscripcion(models.Model):
    id_tipo_suscr = models.IntegerField(primary_key=True)
    nombre_tipo_suscr = models.CharField(max_length=100)
    costo_tipo_suscr = models.IntegerField()

    def __str__(self):
        return self.nombre_tipo_suscr

    class Meta:
        db_table = 'TIPO_SUSCRIPCION'


class Suscripcion(models.Model):
    id_suscr = models.IntegerField(primary_key=True)
    fecha_inicio_sucr = models.DateField()
    fecha_fin_suscr = models.DateField(null=True)
    pagado = models.CharField(max_length=1, default='I')
    id_tipo_suscr = models.ForeignKey('TipoSuscripcion', on_delete=models.CASCADE, db_column='ID_TIPO_SUSCR')

    def __str__(self):
        return f"Suscripción {self.id_suscr}"

    class Meta:
        db_table = 'SUSCRIPCION'


class TipoInmueble(models.Model):
    id_tipo_inmb = models.IntegerField(primary_key=True)
    desc_tipo_inmb = models.CharField(max_length=80)

    def __str__(self):
        return self.desc_tipo_inmb

    class Meta:
        db_table = 'TIPO_INMUEBLE'


class EstadoInmueble(models.Model):
    cod_estado_inmb = models.CharField(max_length=1, primary_key=True, default='L')

    def __str__(self):
        return self.cod_estado_inmb

    class Meta:
        db_table = 'ESTADO_INMUEBLE'


class Inmueble(models.Model):
    id_inmb = models.IntegerField(primary_key=True)
    dir_inmb = models.CharField(max_length=100)
    desc_inmb = models.CharField(max_length=100)
    superficie_inmb = models.DecimalField(max_digits=5, decimal_places=2)
    dormitorio_inmb = models.IntegerField()
    bano_inmb = models.IntegerField()
    precio_inmb = models.IntegerField()
    rut_cli = models.ForeignKey('Cliente', on_delete=models.CASCADE, db_column='RUT_CLI')
    rut_corr = models.ForeignKey('CorredoraPropiedad', on_delete=models.CASCADE, db_column='RUT_CORR')
    id_com = models.ForeignKey('Comuna', on_delete=models.CASCADE, db_column='ID_COM')
    id_ciudad = models.ForeignKey('Ciudad', on_delete=models.CASCADE, db_column='ID_CIUDAD')
    id_region = models.ForeignKey('Region', on_delete=models.CASCADE, db_column='ID_REGION')
    id_tipo_inmb = models.ForeignKey('TipoInmueble', on_delete=models.CASCADE, db_column='ID_TIPO_INMB')
    cod_estado_inmb = models.ForeignKey('EstadoInmueble', on_delete=models.CASCADE, db_column = 'COD_ESTADO_INMB')

    def __str__(self):
        return f"Inmueble {self.id_inmb}"
    
        
    class Meta:
        db_table = 'INMUEBLE'
    



class FotoInmueble(models.Model):
    id_foto_inmb = models.IntegerField(primary_key=True)
    foto_inmb_1 = models.CharField(max_length=100)
    foto_inmb_2 = models.CharField(max_length=100)
    foto_inmb_3 = models.CharField(max_length=100)
    foto_inmb_4 = models.CharField(max_length=100)
    id_inmb = models.ForeignKey('Inmueble', on_delete=models.CASCADE, db_column='ID_INMB')

    class Meta:
        db_table = 'FOTO_INMUEBLE'


class EstadoPublicacion(models.Model):
    desc_estado_pub = models.CharField(max_length=15, default='DISPONIBLE', primary_key=True)

    def __str__(self):
        return self.desc_estado_pub

    class Meta:
        db_table = 'ESTADO_PUBLICACION'


class Publicacion(models.Model):
    id_pub = models.IntegerField(primary_key=True)
    descripcion_pub = models.CharField(max_length=100)
    fecha_pub = models.DateField(auto_now_add=True)
    desc_estado_pub = models.ForeignKey(EstadoPublicacion, on_delete=models.CASCADE, db_column='DESC_ESTADO_PUB')
    id_foto_inmb = models.ForeignKey(FotoInmueble, on_delete=models.CASCADE, db_column='ID_FOTO_INMB')
    id_inmb = models.ForeignKey('Inmueble', on_delete=models.CASCADE, db_column='ID_INMB')
    rut_corr = models.ForeignKey('CorredoraPropiedad', on_delete=models.CASCADE, db_column='RUT_CORR')
    rut_cli = models.ForeignKey('Cliente', on_delete=models.CASCADE, db_column='RUT_CLI')

    class Meta:
        db_table = 'PUBLICACION'


#usuario auth
