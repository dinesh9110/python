def read_file():
    try:
        file_name =(input("Enter filename to read: "))
        with open(file_name,"r") as file:
            content=file.read()
            print(content)
    except FileNotFoundError:
            print("Error: File not found!")
    except IOError:
            print("Error: Unable to read file!")
read_file()