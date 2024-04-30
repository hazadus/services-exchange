from django import forms


class CreateServiceOrderForm(forms.Form):
    """Форма размещения заказа на услугу."""

    service_id = forms.IntegerField()


class OrderChangeStatusForm(forms.Form):
    """Невидимая форма изменения статуса заказа."""

    new_status = forms.CharField()
