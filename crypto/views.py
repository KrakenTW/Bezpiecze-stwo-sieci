import io

from django.http import JsonResponse
from django.views.generic.edit import FormView

from crypto.ciphers.matrix_shift import matrix_encryption
from crypto.ciphers.rail_fence import railfence_encrypt, decrypt_rail_fence
from crypto.ciphers.vigenere import encrypt_vigenere, decrypt_vigenere
from crypto.ciphers.ceasr import crypt_cesar
from crypto.forms import CipherForm, IMPLEMENTED_CIPHERS_CHOICES


class BasicFormView(FormView):
    template_name = "index.html"
    form_class = CipherForm
    success_url = "/"

    # OGOLNY CLEAN
    def form_valid(self, form):
        input = form.cleaned_data.get('input')
        cipher = form.cleaned_data.get('cipher')
        key = form.cleaned_data.get('key')
        file_input = form.cleaned_data.get('input_file')
        if file_input:
            input = io.BytesIO(file_input)
        if self.is_matrix_shift(cipher):
            output = matrix_encryption(input, key)
        elif cipher == IMPLEMENTED_CIPHERS_CHOICES[0][0]:
            output = railfence_encrypt(input, key)
        elif cipher == IMPLEMENTED_CIPHERS_CHOICES[1][0]:
            output = decrypt_rail_fence(input, key)
        elif cipher == IMPLEMENTED_CIPHERS_CHOICES[4][0]:
            output = decrypt_vigenere(input, key)
        elif cipher == IMPLEMENTED_CIPHERS_CHOICES[5][0]:
            output = encrypt_vigenere(input, key)
        elif cipher == IMPLEMENTED_CIPHERS_CHOICES[6][0]:
            # CLEAN NA TO
            output = crypt_cesar(input, key)
        elif cipher == IMPLEMENTED_CIPHERS_CHOICES[7][0]:
            # CLEAN NA TO
            key = 26 - int(key)
            output = crypt_cesar(input, key)

        return JsonResponse({"output": output})

    @staticmethod
    def is_matrix_shift(cipher_name):
        return cipher_name == IMPLEMENTED_CIPHERS_CHOICES[2][0] or cipher_name == IMPLEMENTED_CIPHERS_CHOICES[3][0]
