from django.http import HttpResponse
from django.views.generic.edit import FormView
from crypto.forms import CipherForm


class BasicFormView(FormView):
    template_name = "index.html"
    form_class = CipherForm
    success_url = "/"

    # def post(self, request, *args, **kwargs):
