from django import forms
from django.http import Http404
from django.views.generic.edit import CreateView, DeleteView
from django.shortcuts import render
from .models import Apartment , ApartmentBuilding, ApartmentContact
from .forms import ApartmentForm
from django.views.decorators.clickjacking import xframe_options_exempt
from formtools.wizard.views import CookieWizardView

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

class ApartmentWizard(CookieWizardView):
    template_name = "demo/apartment_wizard.html"
    user = None
    def __init__(self,*args,**kwargs):
        super(ApartmentWizard, self).__init__(*args, **kwargs)
        self.user = kwargs["user"]
    def get_form_kwargs(self, step, *args, **kwargs):
        kwargs = super(ApartmentWizard, self).get_form_kwargs(step, *args, **kwargs)
        if step == "0":
            kwargs['user'] = self.user
        return kwargs
    def done(self, form_list, **kwargs):

        instance = Apartment()

        for form in form_list:
            for key, value in form.cleaned_data.iteritems():
                setattr(instance, key, value)
        instance.save()
	return render(self.request, 'demo/homepage.html', {'apartments': Apartment.objects.all()})

class ApartmentDelete(DeleteView):
    model = Apartment
    success_url = "/"
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(ApartmentDelete, self).get_object()
        if not obj.building.apartment_complex == self.request.user.apartmentcomplexuser.apartment_complex:
            raise Http404
        return obj

class AssignComplexCreate(CreateView):
    def form_valid(self, form):
        form.instance.apartment_complex = self.request.user.apartmentcomplexuser.apartment_complex
        return super(AssignComplexCreate, self).form_valid(form)


class ApartmentContactForm(forms.ModelForm):
    class Meta:
        model = ApartmentContact
        exclude = ['apartment_complex',]

class ApartmentBuildingForm(forms.ModelForm):
    class Meta:
        model = ApartmentBuilding
        exclude = ['apartment_complex',]

class ApartmentContactCreate(AssignComplexCreate):
   model = ApartmentContact
   form_class = ApartmentContactForm

class ApartmentBuildingCreate(AssignComplexCreate):
   model = ApartmentBuilding
   form_class = ApartmentBuildingForm



