from django import forms
from django.core import validators
from prework_app.models import Users

def check_for_z(value):
    if value[0].lower != 'z':
        raise forms.ValidationError('NAME NEEDS TO START WITH Z')

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required = False, widget=forms.HiddenInput,validators = [validators.MaxLengthValidator(0)])

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0 :
            raise forms.ValidationError('Gotcha')
        return botcatcher


class NewUserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
