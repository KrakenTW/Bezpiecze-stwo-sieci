from django import forms

IMPLEMENTED_CIPHERS_CHOICES = [
        ("Railfance encryption", "Railfance encryption"), ("Railfance decryption", "Railfance decryption"),
        ("Matrix shift encryption", 'Matrix shift encryption'), ("Matrix shift decryption", 'Matrix shift decryption'),
        ("Vigenere decryption", 'Vigenere decryption'),("Vigenere encryption", 'Vigenere encryption'),
        ("Cesar decryption", 'Cesar decryption'),("Cesar encryption", 'Cesar encryption'),
    ]


class CipherForm(forms.Form):
    input = forms.CharField()
    key = forms.CharField()
    input_file = forms.FileInput()
    cipher = forms.ChoiceField(choices=IMPLEMENTED_CIPHERS_CHOICES)
