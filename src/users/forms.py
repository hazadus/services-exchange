from django import forms


class UpdateUserBalanceForm(forms.Form):
    """Форма для пополнения баланса пользователя."""

    amount = forms.IntegerField(
        label="Сумма для пополнения",
        help_text="Сумма в рублях, которую вы хотите перевести с карты на баланс",
        min_value=100,
    )
    card_number = forms.IntegerField(
        label="Номер карты",
        help_text="Укажите номер банковской карты, с которой вы хотите пополнить баланс",
    )
