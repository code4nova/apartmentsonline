from django import forms
from .models import Apartment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import PrependedText, AppendedText
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
