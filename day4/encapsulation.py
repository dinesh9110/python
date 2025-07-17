class BankAccount:
    def __init__(self,balance):
        self.__balance=balance #private variable
    def get_balance(self):
        return self.__balance
acc=BankAccount(1000)
print(acc.get_balance())
    