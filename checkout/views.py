from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LcAg6K12YAgEv4TqvUeATq0R8bQDZUcKX1t0D5fHpxYXBsVdFVxCfJeG2Jum2eaqtNjOf7k174O9jrR6nvB0c3u00RrDrQChz',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)