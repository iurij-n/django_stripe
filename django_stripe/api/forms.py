from django import forms

from .models import Сurrency

СURRENCY_ALPHABETIC_CODE = [(code, code) for code in
                            Сurrency.objects.values_list('alphabetic_code',
                                                         flat=True)]


class CurrencySelectForm(forms.Form):
    currency = forms.TypedChoiceField(
        label='',
        choices=СURRENCY_ALPHABETIC_CODE,
        coerce=str
    )
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
