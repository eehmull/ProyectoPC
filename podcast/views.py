from django.shortcuts import render, get_object_or_404, redirect
from .models import Podcasting,Podcast,Podcaster
from django.contrib import messages
from .form import PodcastingForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def listar(request):
    #podcasts = Podcasting.objects.all()
    podcasts = Podcasting.objects.order_by('nombre')
    return render(request, 'podcast/listar.html', {'podcasts': podcasts})

@login_required
def detalle(request, pk):
    pod = get_object_or_404(Podcasting, pk=pk)
    return render(request, 'podcast/detalle.html', {'pod': pod})

#def nuevo(request):
    #formulario = PodcastingForm()
    #return render(request, 'podcast/editar.html', {'formulario': formulario})


@login_required
def nuevo(request):
    if request.method == "POST":
        formulario = PodcastingForm(request.POST)
        if formulario.is_valid():
            podcasting = Podcasting.objects.create(nombre=formulario.cleaned_data['nombre'], descripcion = formulario.cleaned_data['descripcion'],enlace=formulario.cleaned_data['enlace'],)
            for podcaster_id in request.POST.getlist('podcaster'):
                podcast = Podcast(podcaster_id=podcaster_id, podcasting_id = podcasting.id)
                podcast.save()
            #messages.add_message(request, messages.SUCCESS, 'Podcast Guardado Exitosamente')
            return redirect('listar')
    else:
        formulario = PodcastingForm()
    return render(request, 'podcast/editar.html', {'formulario': formulario})

@login_required
def editar(request,pk):
    formulario = get_object_or_404(Podcasting, pk=pk)
    if request.method == "POST":
        formulario = PodcastingForm(request.POST, instance=formulario)
        if formulario.is_valid():
            podcasting = Podcasting.objects.create(nombre=formulario.cleaned_data['nombre'], descripcion = formulario.cleaned_data['descripcion'],enlace=formulario.cleaned_data['enlace'],)
            for podcaster_id in request.POST.getlist('podcaster'):
                podcast = Podcast(podcaster_id=podcaster_id, podcasting_id = podcasting.id)
                podcast.save()
            #messages.add_message(request, messages.SUCCESS, 'Podcast Guardado Exitosamente')
            return redirect('editar', pk=podcast.pk)
    else:
        formulario = PodcastingForm(instance=formulario)
    return render(request, 'podcast/editar.html', {'formulario': formulario})

@login_required
def remover(request, pk):
    formulario = get_object_or_404(Podcasting, pk=pk)
    formulario.delete()
    return redirect('listar')
