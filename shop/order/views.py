from django.shortcuts import render
from django.urls import path, include
from .Controlers import viewsBuyer, viewsProduct, viewsOrder


route_toshop = [
    path("Product/", include(viewsProduct.route_toshopProduct)),
    path("Buyer/", include(viewsBuyer.route_toshopBuyer)),
    path("Order/", include(viewsOrder.route_toshopOrder)),
]