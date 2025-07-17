def access_dict_value():
    try:
        my_dict={"name":"alice","age":25,"city":"new york"}
        k=(input("Enter a key to fetch a value:"))
        print(f"value:{my_dict[k]}")
    except KeyError:
        print("Error: key not found in the dictionary")
access_dict_value()