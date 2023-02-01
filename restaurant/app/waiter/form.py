from app.order import OrderItem
from django import forms


class ChangeOrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity']
