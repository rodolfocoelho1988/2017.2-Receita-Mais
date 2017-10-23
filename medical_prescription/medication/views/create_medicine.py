from django.views.generic import CreateView
from django.urls import reverse

from medication.forms import CreateManipulatedMedicineForm


class CreateMedicineView(CreateView):
    template_name = 'create_manipulated_medicine_form.html'
    sucesss_url = 'list_all_medicines.html'
    form_class = CreateManipulatedMedicineForm

    def get_success_url(self):
        return reverse('list_medicine')

    def form_valid(self, form):
        form.instance.health_professional = self.request.user.healthprofessional
        return super().form_valid(form)
