from django.shortcuts import redirect


def set_user_mode(request):
    """
    Устанавливает режим пользователя - покупатель или продавец, и редиректит на
    указанную страницу.

    Пример использования в шаблоне:
        <a href="{% url 'exchange:set_user_mode' %}?mode=buyer&redirect_to={{ request.path }}">
    """
    mode = request.GET.get("mode", "buyer")
    redirect_to = request.GET.get("redirect_to", "/")

    request.session["user_mode"] = mode

    return redirect(redirect_to)
