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
    class Meta:
        model = Apartment
        fields = ["owned_by","managed_by","phone_contact","address"]


class AptWiz_2(forms.ModelForm):
    class Meta:
        model = Apartment
	fields = ["property_name","number_of_bedrooms","max_occupants"]

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
	fields = ["lease_term","maximum_income","minimum_income","rent","income_divisor"]

class AptWiz_4(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ["bus_transit","rail_transit"]

