from django.views.generic.edit import CreateView
from django.shortcuts import render
from .models import Apartment
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
