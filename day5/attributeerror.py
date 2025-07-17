def handle_attribute_error():
    try:
        num=10
        num.append(5)
    except AttributeError:
        print("Error :'int' object has no attribute 'append'!")
handle_attribute_error()