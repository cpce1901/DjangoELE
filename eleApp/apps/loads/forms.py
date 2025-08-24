from django import forms

class ExcelUploadForm(forms.Form):
    file = forms.FileField(
        label="Selecciona un archivo Excel",
        help_text="Formatos permitidos: .xls, .xlsx",
        widget=forms.ClearableFileInput(attrs={"class": "form-control"})
    )

    def clean_file(self):
        uploaded_file = self.cleaned_data['file']
        if not uploaded_file.name.endswith(('.xls', '.xlsx')):
            raise forms.ValidationError("El archivo debe ser en formato .xls o .xlsx")
        return uploaded_file
