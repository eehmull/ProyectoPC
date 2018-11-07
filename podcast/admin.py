
from django.contrib import admin
from .models import Podcaster, PodcasterAdmin, Podcasting, PodcastingAdmin

#Registramos nuestras clases principales.
admin.site.register(Podcaster, PodcasterAdmin)
admin.site.register(Podcasting, PodcastingAdmin)
