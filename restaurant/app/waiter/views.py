from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Sum, Count, Avg
from django.views.generic import ListView, DetailView
from app.order.models import OrderItem, Order, Rating
from app.menu.models import Dish
from app.waiter.models import Waiter, Tips
from app.menu.filter import MenuFilter
from django.contrib.auth.mixins import LoginRequiredMixin


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    queryset = Order.objects.select_related('waiter').select_related('customer')
    context_object_name = 'order_list'
    template_name = 'waiter/order_list.html'

    def post(self, request, *args, **kwargs):
        if self.request.POST:
            waiter = self.request.POST.get('waiter_id')
            order = self.request.POST.get('order_id')
            if waiter:
                Order.objects.filter(id=order).update(waiter_id=waiter)
            return JsonResponse('Ok', safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['waiter_list'] = Waiter.objects.all()
        return context


class InterfaceView(LoginRequiredMixin, DetailView, ListView):
    model = Order
    queryset = Order.objects.select_related('customer')
    context_object_name = 'order'
    template_name = 'waiter/order_detail/order_detail.html'

    def post(self, request, *args, **kwargs):
        if self.request.POST:
            quantity = self.request.POST.get('quantity')
            item_id = self.request.POST.get('item_id')
            dish_id = self.request.POST.get('dish_id')
            order_id = self.request.POST.get('order_id')
            status_order_id = self.request.POST.get('status_order_id')
            order_status = self.request.POST.get('order_status')
            if status_order_id:
                Order.objects.filter(id=status_order_id).update(status=order_status)
            if order_id and not OrderItem.objects.filter(order_id=order_id, dish_id=dish_id):
                OrderItem.objects.create(dish_id=dish_id, order_id=order_id, quantity=1)
            if quantity and int(quantity) > 0:
                OrderItem.objects.filter(id=item_id).update(quantity=quantity)
            elif quantity and int(quantity) == 0:
                OrderItem.objects.filter(id=item_id).delete()
            return JsonResponse({'quantity': quantity})

    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        context = super().get_context_data(**kwargs)
        context['dish'] = Dish.objects.all()
        context['filter'] = MenuFilter(self.request.GET, queryset=Dish.objects.all())
        context['order_item'] = OrderItem.objects.all().filter(order_id=context['order'].id)
        a = context['order_item'].select_related('order').select_related('dish')
        context['order_item'] = a
        context['table'] = ''
        context['total'] = 0
        context['status'] = []
        for i in context['order'].get_all_status():
            context['status'].append(i[0])
        for i in context['order_item']:
            context['total'] += i.get_total()
            break
        return context


class TipsDetailView(LoginRequiredMixin, ListView):
    model = Tips
    context_object_name = 'tips'
    template_name = 'waiter/tips/waiter_tips.html'

    def get_queryset(self):
        return Tips.objects.filter(waiter__user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['orders'] = Order.objects.filter(waiter__user=self.request.user).all()
        context['total_amount'] = context['tips'].aggregate(total_amount=Sum('amount'))['total_amount']
        context['count_order'] = context['orders'].aggregate(order_count=Count('id'))['order_count']
        return context


class RestaurantStatsDetailView(LoginRequiredMixin, ListView):
    model = Order
    queryset = Order.objects.filter(status='Оплачено').all().select_related('waiter').select_related('rating')
    context_object_name = 'orders'
    template_name = 'waiter/admin_page/stats.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['total_amount'] = context['orders'].aggregate(total_amount=Sum('total_payment'))['total_amount']
        context['count_order'] = context['orders'].aggregate(order_count=Count('id'))['order_count']
        context['average_rating'] = int(Rating.objects.all().aggregate(average_rating=Avg('rating'))['average_rating'])
        return context
