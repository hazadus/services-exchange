from django import forms


class MessageCreateForm(forms.Form):
    """Форма создания сообщения."""

    topic_ct = forms.CharField()
    topic_id = forms.IntegerField()
    recipient_id = forms.IntegerField()
    text = forms.CharField()
    # TODO: implement file field
    # file = forms.FileField()
