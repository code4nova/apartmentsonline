from django import forms
from .models import Apartment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import PrependedText, AppendedText
from django.db import models
import models

class ApartmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ApartmentForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper['rent'].wrap(PrependedText, '$')
        self.helper['minimum_income'].wrap(PrependedText, '$')
        self.helper['maximum_income'].wrap(PrependedText, '$')
        self.helper['lease_term'].wrap(AppendedText, 'months')
        self.helper.form_tag = False
    class Meta:
        model = Apartment
        fields = "__all__"

class AptWiz_1(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super(AptWiz_1, self).__init__(*args, **kwargs)
        # access object through self.instance..i.
        self.fields['building'].queryset = models.ApartmentBuilding.objects.filter(apartment_complex=user.apartmentcomplexuser.apartment_complex)
        self.fields['contact'].queryset = models.ApartmentContact.objects.filter(apartment_complex=user.apartmentcomplexuser.apartment_complex)
    class Meta:
        model = Apartment
        fields = ["building","contact","suite_number"]


class AptWiz_2(forms.ModelForm):
    class Meta:
        model = Apartment
        num_bedchoices = ((0,"Studio"),(1,"One Bedroom"), (2, "Two Bedroom"), (3,"Three Bedroom"))
        num_occupantchoices = ((1,"One"), (2, "Two"), (3,"Three"),(4,"Four"),(5, "Five"))
        widgets = {'number_of_bedrooms': forms.Select(choices=num_bedchoices),
                   'max_occupants': forms.Select(choices=num_occupantchoices)}
        fields = ["number_of_bedrooms","max_occupants"]

class AptWiz_3(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AptWiz_3, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper['rent'].wrap(PrependedText, '$')
        self.helper['minimum_income'].wrap(PrependedText, '$')
        self.helper['maximum_income'].wrap(PrependedText, '$')
        self.helper['lease_term'].wrap(AppendedText, 'months')
        self.helper.form_tag = False

    class Meta:
        model = Apartment
	fields = ["lease_term","maximum_income","minimum_income","rent"]

class AptWiz_4(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ["bus_transit","rail_transit"]

