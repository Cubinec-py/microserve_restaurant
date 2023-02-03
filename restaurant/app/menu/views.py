from django.views.generic import ListView
from .filter import MenuFilter
from app.cart.utils import cart_data
from app.order.utils import cookie_items
from app.order.models import Customer, Order
from django.shortcuts import get_object_or_404
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
        order = data['order']
        customer = cookie_items(self.request)
        try:
            customer_id = get_object_or_404(Customer, first_name=customer['first_name'], last_name=customer['last_name'])
            context['order_id'] = get_object_or_404(Order, customer=customer_id)
            context['customer'] = customer_id
        except:
            pass
        context['items'] = items
        context['order'] = order
        context['filter'] = MenuFilter(self.request.GET, queryset=self.get_queryset())
        return context
