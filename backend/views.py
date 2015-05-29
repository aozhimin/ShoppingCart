import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .models import Product, Price
from fastcart.models import Cart, CartManager

@csrf_protect
def view_cart(request):  
    # cart = request.session.get("cart", None)
    product_list =  list(Product.objects.all())
    # cartManager = CartManager()
    # cart = cartManager.get_for_request(request)
    cart = Cart()
    cart.save()

    price_dict = {}
    for product in product_list:
    	cart.add(product)
        # price_dict('product_id') = price.product.id
        # price_list = Price.objects.filter(product__in=product_li


    cart.save()
    # for item in cart.get_items():
    #     config_list = item.get_config_type_list()
    #     import pdb;pdb.set_trace()

    # for price in price_list:
    #     price_dict('product_id') = price.product.id
    #     price_dict('unit_price') = price.unit_price

    # import pdb;pdb.set_trace()

  
    # if not cart:  
    #     cart = Cart()  
        # request.session["cart"] = json.dumps(cart)
                   
    return render(request, 'base.html', {'cart': cart})