from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError, JsonResponse
from django.urls import path
from ..ServiceShop import serviceProduct
from ..models import Product
from django.core.serializers.json import DjangoJSON
import unittest

def _index(request):
    if request.method =="GET":
        return HttpResponse(_getAll(request))
    if request.method == "POST":
        return HttpResponse(_post(request))
    return HttpResponseBadRequest("Bad Request")
    

def _getAll(request, Id):
    return serviceProduct.get(request, Id)

def _post(request):
    try:
        prod = serviceProduct.post(request.POST)
        return HttpResponse(prod)
    except serviceProduct.ValidateExeption:
        return HttpResponse(prod)
    except:
        return HttpResponseServerError()
    
def _indexId(request, Id):
    if not Id>0:
        return HttpResponseBadRequest("Bad Request id not valid") 
    if request.method == "GET":
        return HttpResponse(_get(request, Id))
    if request.method == "PUT":
        return HttpResponse(_put(request, Id))
    if request.method == "DELETE":
        return HttpResponse(_del(request, Id))
    return HttpResponseBadRequest("Bad Request")

def _get(request, Id):
    try:
        return serviceProduct.get(request.body, Id)
    except Product.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()


def _put(request, Id):
    if not Id>0:
        return HttpResponseBadRequest("Bad Request")
    try:
        return serviceProduct.update(request.body, Id)
    except Product.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()
    

def _del(request, Id):
    try:
        serviceProduct.delete(request,Id)
        return HttpResponse()
    except Product.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()
    
def _search(request):
    try:
        return serviceProduct.search(request.GET)
    except Product.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()


route_toshop = [
    path("", _index),
    path("<int:Id>", _indexId),
    path("search", _search),
]