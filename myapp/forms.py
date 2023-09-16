from django import forms
from .models import Stagiaire


class StagiaireFroms(forms.ModelForm):
    class Meta:
        model=Stagiaire
        fields=('stgMatricule','fullName','mobile','filiere')


    def __init__(self, *args, **kwargs):
            super(StagiaireFroms,self).__init__(*args, **kwargs)
            self.fields['filiere'].empty_label = "Select"
            # self.fields['emp_code'].required = False