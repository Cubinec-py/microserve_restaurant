from .models import Order, OrderItem, Tips
from django.views.generic import DetailView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/pay_order.html'
    context_object_name = 'order'

    def post(self, request, *args, **kwargs):
        if self.request.POST:
            order_id = self.request.POST.get('id_order')
            total = self.request.POST.get('total')
            tips = self.request.POST.get('tips')
            if order_id:
                order = get_object_or_404(Order, id=order_id)
                tips = Tips.objects.create(amount=float(tips), customer_id=order.customer.id)
                order.tips = tips
                order.total_payment = float(total)
                order.status = 'Оплачено'
                order.save()
                return JsonResponse('Ok', safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = OrderItem.objects.filter(order_id=context['order'].id)
        context['total'] = 0
        context['quantity'] = 0
        for i in context['items']:
            context['quantity'] += i.quantity
            context['total'] += i.get_total()
        return context
