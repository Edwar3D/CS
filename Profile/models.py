from django.db import models
from django.utils import timezone

class ModelCiudad (models.Model):
    ciudad = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ciudad

    class Meta:
        db_table = 'Ciudad'

class ModelOcupacion (models.Model):    
    ocupacion = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ocupacion

    class Meta:
        db_table = 'Ocupacion'


class ModelGenero (models.Model):
    genero = models.CharField(max_length=50, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.genero

    class Meta:
        db_table = 'Genero'

class ModelEstado (models.Model):    
    estado = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.estado

    class Meta:
        db_table = 'Estado'


class ModelEstadoCivil (models.Model):
    estadoCivil = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.estadoCivil

    class Meta:
        db_table = 'EstadoCivil'



class Profile (models.Model):
    nombre = models.CharField(max_length=254, null=False)
    apPat = models.CharField(max_length=254, null=False)
    apMat = models.CharField(max_length=254, null=False)
    edad = models.IntegerField( null=False)
    ciudad = models.ForeignKey(ModelCiudad,on_delete=models.CASCADE)  
    estado = models.ForeignKey(ModelEstado,on_delete=models.CASCADE)  
    genero =models.ForeignKey(ModelGenero,on_delete=models.CASCADE)    
    ocupacion =models.ForeignKey(ModelOcupacion,on_delete=models.CASCADE)    
    estadoCivil =models.ForeignKey(ModelEstadoCivil,on_delete=models.CASCADE)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

def __str__(self):
    return self.nombre

class Meta:
    db_table = 'Profile'