num=int(input("enter a number up to which table you want"))
for i in range(1,num+1):
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
    print("\t")