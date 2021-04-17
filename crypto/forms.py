from django import forms


class CipherForm(forms.Form):
    input = forms.CharField()
    cipher = forms.ChoiceField(choices=[("a", "a"), ("b", "b")])
