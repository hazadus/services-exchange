from django import forms


class OfferCreateForm(forms.Form):
    """Невидимая форма создания предложения на выполнение проекта."""

    project_id = forms.IntegerField()


class OfferSetStatusForm(forms.Form):
    """Невидимая форма изменения статуса предложения на выполнение проекта."""

    new_status = forms.CharField()
