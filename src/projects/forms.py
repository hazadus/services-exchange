from django import forms


class CreateOfferForm(forms.Form):
    """Невидимая форма создания предложения на выполнение проекта."""

    project_id = forms.IntegerField()
