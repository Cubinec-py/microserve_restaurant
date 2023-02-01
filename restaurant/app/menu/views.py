from django.views.generic import ListView
from .filter import MenuFilter
from app.cart.utils import cart_data

from .models import Dish


class ShowMenuListView(ListView):
    model = Dish
    paginate_by = 12
    context_object_name = 'dish'
    template_name = 'menu/menu_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = cart_data(self.request)

        items = data['items']
        context['items'] = items
        context['filter'] = MenuFilter(self.request.GET, queryset=self.get_queryset())
        return context
