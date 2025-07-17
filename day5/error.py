def access_list_element():
    try:
        my_list=[1,2,3,4,5]
        i=int(input("Enter index to access:"))
        print(f"Element:{my_list[i]}")
    except IndexError:
        print("Error:Index out of range")
    except ValueError:
        print("Error: Invalid input! Enter an integer")
access_list_element()