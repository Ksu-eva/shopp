from ..models import Order
from datetime import *
from dateutil.relativedelta import relativedelta


class ValidateExeption(Exception):
    pass

def get(Id=0):
    if Id==0:
        return SerialiseList(Order.objects.all())
    ord = Order.objects.get(id = Id)
    return Serialise(ord)

def Serialise(order):
    return "{"+f"id:{order.id}, date_delivery:{order.date_delivery}, type_of_delivery:{order.type_of_delivery}, adress:{order.adress}, set_product:{order.set_product}"+"}"

def SerialiseList(orders):
    jsonResult = "["
    for g in orders:
        jsonResult+=Serialise(g)+","
    jsonResult+="]"
    return jsonResult

def Deserialise(JsonOrder):
    order = order()
    Order.date_delivery = JsonOrder.get("date_delivery")
    Order.type_of_delivery = JsonOrder.get("type_of_delivery")
    Order.adress = JsonOrder.get("adress")
    Order.set_product = JsonOrder.get("set_product")
    return Order                            

def Validate(order):
    if len(order.type_of_delivery) >50:
        raise ValidateExeption()
    date_delivery = order.date_delivery(1000, 1, 1)
    date_now = datetime.now()
    delta = relativedelta(date_delivery, date_now)
    if order.date_delivery==0:
        delta = date_now
        return(delta)
    if delta < 0:
        raise ValueError("Incorrect date_delivery")
    if delta >0:
        raise ValidateExeption()
                                 
def post(JsonOrder):
    entity = Deserialise(JsonOrder)
    Validate(entity)
    entity.save()
    return Serialise(entity)

def update(JsonOrder, Id):
    entity = Deserialise(JsonOrder)
    Validate(entity)
    ord = Order.objects.get(id = Id)
    ord.date_delivery = entity.date_delivery
    ord.type_of_delivery = entity.type_of_delivery
    ord.adress = entity.adress
    ord.set_product = entity.set_product
    ord.save

def delete(Id):
    ord = Order.objects.get(id = Id)
    ord.delete()

def search(query):
    _id = query.get("id", 0)
    filt = Order.objects.all()
    if id>0:
        filt = filt.filter(id = id)
    _date_delivery = query.get("date_delivery", "")
    _date_now = query.get("date_now", "")
    _type_of_delivery = query.get("type_of_delivery", "")
    _adress = query.get("_adress", "")
    _set_product = query.get("set_product", "")
    if _date_delivery>= _date_now and _type_of_delivery!= "" and _adress!= "" and _set_product!= "":
        filt = filt.filter(date_delivery = _date_delivery, date_now = _date_now, type_of_delivery = _type_of_delivery, adress = _adress, set_product = _set_product)
    return SerialiseList(filt)