def NULL_not_found(object: any) -> int:
    obj_type = type(object)
    if object is None:
        print("Nothing: ", object, " ", obj_type)
    elif isinstance(object, float) and object != object:
        print("Cheese: ", object, " ", obj_type)
    elif object == 0:
        print("Zero: ", object, " ", obj_type)
    elif object == '':
        print("Empty: ", " ", obj_type)
    elif object is False:
        print("Fake: ", object, " ", obj_type)
    else:
        print("Type not Found")
        return 1
    return 0
