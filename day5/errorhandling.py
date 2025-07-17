def divide_numbers():
    try:
        n1=int(input("Enter numerator"))
        n2=int(input("Enter denominator"))
        res=n1/n2
    except ZeroDivisionError:
        print("Error: Cannot divide by Zero!")
    except ValueError:
        print("Error:Invalid input! Enter integers only!")
    else:
        print(f"Result:{res}")
    finally:
        print("Execution completed")
divide_numbers()