# catalogue/views/representation.py
from django.shortcuts import render, get_object_or_404, redirect
from catalogue.models import Representation, Spectacle, Location
from catalogue.forms import RepresentationForm
from django.utils import timezone

def representation_list(request):
    representations = Representation.objects.all()
    return render(request, 'representation/representation_list.html', {'representations': representations})

def representation_detail(request, pk):
    representation = get_object_or_404(Representation, pk=pk)
    return render(request, 'representation/representation_detail.html', {'representation': representation})

def representation_create(request):
    if request.method == "POST":
        form = RepresentationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('representation_list')
    else:
        form = RepresentationForm()
    return render(request, 'representation/representation_form.html', {'form': form})

def representation_update(request, pk):
    representation = get_object_or_404(Representation, pk=pk)
    if request.method == "POST":
        form = RepresentationForm(request.POST, instance=representation)
        if form.is_valid():
            form.save()
            return redirect('representation_list')
    else:
        form = RepresentationForm(instance=representation)
    return render(request, 'representation/representation_form.html', {'form': form})
