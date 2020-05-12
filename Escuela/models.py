from django.db import models

# Create your models here.



class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    appaterno = models.CharField(max_length=30)
    apmaterno = models.CharField(max_length=30)
    curp = models.CharField(max_length=18)
    tutor = models.CharField(max_length=40)
    matricula= models.CharField(max_length=10, primary_key= True,verbose_name='Numero de Matricula')
    SEXO=(('F','Femenino'),('M','Masculino')) #se hace arreglo
    Sexo = models.CharField(max_length=1,choices=SEXO,default='M')
    fecha_nacimiento= models.DateField()
    
    def __str__(self):
        return "%s %s %s %s %s" % (self.nombre, self.appaterno, self.apmaterno, self.curp, self.matricula)

class Gradogrupo(models.Model):
    inscrito = models.BooleanField()
    grupo = models.IntegerField(default=1)
    grado = models.CharField(max_length=1,default='A')
    matriculaFK=models.ForeignKey(Alumno,on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (self.inscrito, self.matriculaFK, self.grado)
