from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError, HttpResponseRedirect, JsonResponse
from django.urls import path
from ..ServiceShop import serviceOrder
from ..models import Order

def _index(request):
    if request.method =="GET":
        return HttpResponse(_getAll(request))
    if request.method == "POST":
        return HttpResponse(_post(request))
    return HttpResponseBadRequest("Bad Request")


def _getAll(request, Id):
    return serviceOrder.get(request, Id)

def _post(request):
    try:
        ord = serviceOrder.post(request.POST)
        return HttpResponse(ord)
    except serviceOrder.ValidateExeption:
        return HttpResponse(ord)
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
        return serviceOrder.get(request, Id)
    except Order.DoesNotExist:
        return HttpResponseNotFound()


def _put(request, Id):
    if not Id>0:
        return HttpResponseBadRequest("Bad Request")
    try:
        return serviceOrder.update(request.POST, Id)
    except Order.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()
    

def _del(request, Id):
    if not Id>0:
        return HttpResponseBadRequest("Bad Request")
    try:
        return serviceOrder.delete(request.POST, Id)
    except Order.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()
    
def _search(request):
    try:
        return serviceOrder.search(request.GET)
    except Order.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()


route_toshop = [
    path("", _index),
    path("<int:Id>", _indexId),
    path("search", _search),
]