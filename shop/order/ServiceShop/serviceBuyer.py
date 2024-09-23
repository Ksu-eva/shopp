from ..models import Buyer


class ValidateException(Exception):
    pass

def get(Id=0):
    if Id==0:
        return SerialiseList(Buyer.objects.all())
    buy = Buyer.objects.get(id = Id)
    return Serialise(buy)

def Serialise(buyer):
    return "{"+f"id:{buyer.id}, name:{buyer.name}, firstName:{buyer.firstName}, lastName:{buyer.lastName}, adress:{buyer.adress}"+"}"

def SerialiseList(buyers):
    jsonResult = "["
    for g in buyers:
        jsonResult+=Serialise(g)+","
    jsonResult+="]"
    return jsonResult

def Deserialise(JsonBuyer):
    Buyer()
    Buyer.name = JsonBuyer.get("name")
    Buyer.firstName = JsonBuyer.get("firstName")
    Buyer.lastName = JsonBuyer.get("lastName")
    Buyer.adress = JsonBuyer.get("adress")
    return Buyer                            

def Validate(buyer):
    if len(buyer.name) >50:
        raise ValidateException()
    elif len(buyer.firstName) >50:
        raise ValidateException()
    elif len(buyer.lastName) >50:
        raise ValidateException()
    elif len(buyer.adress) >200:
        raise ValidateException()
        
def post(JsonBuyer):
    entity = Deserialise(JsonBuyer)
    Validate(entity)
    entity.save()
    return Serialise(entity)

def update(JsonBuyer, Id):
    entity = Deserialise(JsonBuyer)
    Validate(entity)
    buy = Buyer.objects.get(id = Id)
    buy.name = entity.name
    buy.firstName = entity.firstName
    buy.lastName = entity.lastName
    buy.adress = entity.adress
    buy.save

def delete(Id):
    buy = Buyer.objects.get(id = Id)
    buy.delete()

def search(query):
    _id = query.get("id", 0)
    filt = Buyer.objects.all()
    if id>0:
        filt = filt.filter(id = id)
    _name = query.get("name", "")
    _firstName = query.get("firstName", "")
    _lastName = query.get("lastName", "")
    _adress = query.get("adress", "")
    if _name!= "" and _firstName!= "" and _lastName!= "" and _adress!= "":
        filt = filt.filter(name = _name, firstName = _firstName, lastName = _lastName, adress = _adress)
    return SerialiseList(filt)