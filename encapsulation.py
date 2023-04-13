class BankAccount:
    def __init__(self, holder, balance):
        self._holder = holder # protected --> no error when accessing directly, but indicates it shouldn't be
        self.__balance = balance # private --> error when accessing directly, but can be by public methods

    def get_balance(self):
        print(self.__balance)

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

# using these access modifiers is encapsulation. We hide the implementation details of the class from public view to keep the code maintainable and secure.

# get_balance, deposit, and withdraw are public ways to access the private attribute balance, but accessing balance directly would throw an error.