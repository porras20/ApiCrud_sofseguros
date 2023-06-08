from django.db import models

# Create your models here.
from django.core.validators import MaxValueValidator

class User(models.Model):
    name = models.CharField(max_length=255)
    numero_documento = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    email = models.EmailField(max_length=100)
    fecha_nacimiento = models.DateField()
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.email
