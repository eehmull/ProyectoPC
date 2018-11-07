from django.shortcuts import render, get_object_or_404, redirect
from .models import Podcasting

# Create your views here.
def listar(request):
    #podcasts = Podcasting.objects.all()
    podcasts = Podcasting.objects.order_by('nombre')
    return render(request, 'podcast/listar.html', {'podcasts': podcasts})

def detalle(request, pk):
    pod = get_object_or_404(Podcasting, pk=pk)
    return render(request, 'podcast/detalle.html', {'pod': pod})
