from django.urls import path
from crypto.views import BasicFormView

urlpatterns = [
    path('', BasicFormView.as_view()),
]