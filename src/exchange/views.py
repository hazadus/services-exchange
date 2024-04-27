from django.shortcuts import redirect
from django.views.generic import ListView

from exchange.models import Category
from exchange.selectors import category_list


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


class CategoryListView(ListView):
    model = Category
    template_name = "exchange/category_list.html"

    def get_queryset(self):
        return category_list()
