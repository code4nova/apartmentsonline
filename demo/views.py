from django.views.generic.edit import CreateView
from django.shortcuts import render
from .models import Apartment
from .forms import ApartmentForm
from django.views.decorators.clickjacking import xframe_options_exempt


def homepage(request):
    apartments = Apartment.objects.all()
    context = {'apartments': apartments}
    return render(request, 'demo/homepage.html', context)


@xframe_options_exempt
def embed(request):
    if request.GET.get("filterm") != None:
        apartments = Apartment.objects.filter(managed_by_id=request.GET.get("filterm"))
    elif request.GET.get("filtero") != None:
        apartments = Apartment.objects.filter(owned_by_id=request.GET.get("filtero"))
    else:
        apartments = Apartment.objects.all()
    context = {'apartments': apartments}
    return render(request, 'demo/embed/embed_full.html', context)

class  ApartmentCreate(CreateView):
    form_class = ApartmentForm
    template_name = "demo/apartment_form.html"
    success_url = "/"
