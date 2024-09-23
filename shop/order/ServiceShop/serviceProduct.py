from ..models import Product


class ValidateExeption(Exception):
    pass

def get(Id=0):
    if Id==0:
        return SerialiseList(Product.objects.all())
    prod = Product.objects.get(id = Id)
    return Serialise(prod)

def Serialise(product):
    return "{"+f"id:{product.id}, name_pr:{product.name_pr}, cost:{product.cost}"+"}"

def SerialiseList(products):
    jsonResult = "["
    for g in products:
        jsonResult+=Serialise(g)+","
    jsonResult+="]"
    return jsonResult

def Deserialise(JsonProduct):
    product = product()
    Product.name_pr = JsonProduct.get("name_pr")
    Product.cost = JsonProduct.get("cost")
    return Product                            

def Validate(product):
    if len(product.name_pr) >50:
        raise ValidateExeption()
    if product.cost>0:
        raise ValidateExeption()
    else:
        raise ValueError("Incorrect cost")
    
def post(JsonProduct):
    entity = Deserialise(JsonProduct)
    Validate(entity)
    entity.save()
    return Serialise(entity)

def update(JsonProduct, Id):
    entity = Deserialise(JsonProduct)
    Validate(entity)
    prod = Product.objects.get(id = Id)
    prod.name_pr = entity.name_pr
    prod.cost = entity.cost
    prod.save

def delete(Id):
    prod = Product.objects.get(id = Id)
    prod.delete()

def search(query):
    _id = query.get("id", 0)
    filt = Product.objects.all()
    if id>0:
        filt = filt.filter(id = id)
    _name_pr = query.get("name_pr", "")
    _cost = query.get("cost", "")
    if _name_pr!= "" and _cost>0:
        filt = filt.filter(name_pr = _name_pr, cost = _cost)
    return SerialiseList(filt)