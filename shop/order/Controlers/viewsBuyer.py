from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError, HttpResponseRedirect, JsonResponse
from django.urls import path
from ..ServiceShop import serviceBuyer
from ..models import Buyer

def _index(request):
    if request.method =="GET":
        return HttpResponse(_getAll(request))
    if request.method == "POST":
        return HttpResponse(_post(request))
    return HttpResponseBadRequest("Bad Request")


def _getAll(request, Id):
    return serviceBuyer.get(request, Id)

def _post(request):
    try:
        buy = serviceBuyer.post(request.POST)
        return HttpResponse(buy)
    except serviceBuyer.ValidateException:
        return HttpResponse(buy)
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
        return serviceBuyer.get(request, Id)
    except Buyer.DoesNotExist:
        return HttpResponseNotFound()


def _put(request, Id):
    if not Id>0:
        return HttpResponseBadRequest("Bad Request")
    try:
        return serviceBuyer.update(request.POST, Id)
    except Buyer.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()
    

def _del(request, Id):
    if not Id>0:
        return HttpResponseBadRequest("Bad Request")
    try:
        return serviceBuyer.delete(request.POST, Id)
    except Buyer.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()
    
def _search(request):
    try:
        return serviceBuyer.search(request.GET)
    except Buyer.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()


route_toshop = [
    path("", _index),
    path("<int:Id>", _indexId),
    path("search", _search),
]