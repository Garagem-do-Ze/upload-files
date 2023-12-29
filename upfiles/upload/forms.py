from django import forms

class DocumentForm(forms.Form):
    first_name = forms.CharField(max_length=220)
    second_name = forms.CharField(max_length=220)
    docname = forms.CharField(max_length=220)
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )



