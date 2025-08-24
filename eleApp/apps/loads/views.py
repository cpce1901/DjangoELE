import pandas as pd
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ExcelUploadForm

class LoadTemplateView(FormView):
    template_name = 'loads/load_file.html'
    form_class = ExcelUploadForm
    success_url = reverse_lazy('load_file')  # redirige a la misma vista

    def form_valid(self, form):
        file = self.request.FILES['file']
        try:
            df = pd.read_excel(file)
            print(df)
        except Exception as e:
            print(e)
        return super().form_valid(form)
