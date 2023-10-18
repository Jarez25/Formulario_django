from django.db import models

# Create your models here.

class Question(models.Model):
    questio_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
class Choice (models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Usuario(models.Model):
    # Campos de texto (CharField es para guardar candenas de texto)
    nombre_usuario = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    # Campos numéricos (IntergerField y FloatField son para guardar campos de enteros y decimales)
    edad = models.PositiveIntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.FloatField()

    # Campos de fechas (DateField y DateTimeField se ocupan para guardar fecha y el otro fecha y hora)
    fecha_nacimiento = models.DateField()
    ultimo_login = models.DateTimeField(auto_now=True)

    # Campos booleanos (BooleanField este es para valores boleanos(True o Flase))
    esta_activa = models.BooleanField(default=True)
    es_personal = models.BooleanField(default=False)

    # Campos con opciones
    OPCIONES_ROL = [
        ('usuario', 'Usuario normal'),
        ('admin', 'Administrador'),
    ]
    roles = models.CharField(max_length=7, choices=OPCIONES_ROL, default='usuario')