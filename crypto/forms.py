from django import forms

IMPLEMENTED_CIPHERS_CHOICES = [
        ("Railfance encryption", "Railfance encryption"), ("Railfance decryption", "Railfance decryption"),
        ("Matrix shift encryption", 'Matrix shift encryption'), ("Matrix shift decryption", 'Matrix shift decryption'),
        ("Vigenere decryption", 'Vigenere decryption'), ("Vigenere encryption", 'Vigenere encryption'),
        ("Cesar encryption", 'Cesar encryption'), ("Cesar decryption", 'Cesar decryption'),
        ("Matrix encryption", 'Matrix encryption'), ("Matrix decryption", 'Matrix decryption'),
        ("Stream encryption", 'Stream encryption'), ("Stream decryption", 'Stream decryption'),
    ]


class CipherForm(forms.Form):
    input = forms.CharField()
    key = forms.CharField()
    input_file = forms.FileField(required=False)
    cipher = forms.ChoiceField(choices=IMPLEMENTED_CIPHERS_CHOICES)
