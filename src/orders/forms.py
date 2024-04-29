from django import forms


class CreateServiceOrderForm(forms.Form):
    """Форма размещения заказа на услугу."""

    service_id = forms.IntegerField()
