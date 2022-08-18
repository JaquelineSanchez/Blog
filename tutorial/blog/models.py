from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Titulo")
    content = models.TextField(verbose_name = "Contenido")

    def __str__(self):
        return self.title