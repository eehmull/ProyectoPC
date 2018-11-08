from django.db import models
from django.utils import timezone
from django.contrib import admin
# Create your models here.

class Podcaster(models.Model):

    nombre  =   models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()


    def __str__(self):

        return self.nombre

class Podcasting(models.Model):
    nombre    = models.CharField(max_length=60)

    descripcion      = models.TextField()

    enlace    = models.CharField(max_length=150)

    #fecha_creacion = models.DateTimeField(
    #        default=timezone.now)
    #fecha_publicacion = models.DateTimeField(
    #        blank=True, null=True)

    podcaster   = models.ManyToManyField(Podcaster, through='Podcast')

    def publicar(self):
        #self.fecha_publicacion = timezone.now()
        self.save()



    def __str__(self):

        return self.nombre

class Podcast (models.Model):

    podcaster = models.ForeignKey(Podcaster, on_delete=models.CASCADE)

    podcasting = models.ForeignKey(Podcasting, on_delete=models.CASCADE)

class PodcastInLine(admin.TabularInline):

    model = Podcast

#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.

    extra = 1


class PodcasterAdmin(admin.ModelAdmin):

    inlines = (PodcastInLine,)


class PodcastingAdmin (admin.ModelAdmin):

    inlines = (PodcastInLine,)
