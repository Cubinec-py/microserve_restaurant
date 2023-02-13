from .models import Order, OrderItem, Rating
from app.menu.models import Dish
from django.views.generic import DetailView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from app.waiter.models import Tips
from .tasks import update_dish_amount


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/pay_order.html'
    context_object_name = 'order'

    def post(self, request, *args, **kwargs):
        order_id = self.request.POST.get('id_order')
        total = self.request.POST.get('total')
        tips = self.request.POST.get('tips')
        rate_amount = self.request.POST.get('rate_amount')
        if order_id:
            order = get_object_or_404(Order, id=order_id)
            order_items = OrderItem.objects.filter(order_id=order_id).all()
            for item in order_items:
                quantity = item.quantity
                dish = Dish.objects.get(id=item.dish.id)
                if 0 < dish.amount and quantity <= dish.amount:
                    dish.amount -= quantity
                    dish.save()
                    print(dish.id, dish.amount)
                    update_dish_amount.delay(dish.id, dish.amount)
                elif quantity > dish.amount or dish.amount == 0:
                    dish.amount = 0
                    dish.status = 'Не доступно'
                    dish.save()
                    print(dish.id, dish.amount)
                    update_dish_amount.delay(dish.id, dish.amount)
            if rate_amount:
                Rating.objects.create(rating=int(rate_amount), order_id=order_id)
            if tips:
                tips = Tips.objects.create(amount=float(tips), waiter_id=order.waiter_id)
                order.tips = tips
            order.total_payment = float(total)
            order.status = 'Оплачено'
            order.save()
            return JsonResponse('Ok', safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = OrderItem.objects.filter(order_id=context['order'].id)
