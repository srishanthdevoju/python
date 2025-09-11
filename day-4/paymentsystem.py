class Payment:
    def pay(self,amount):
        print("Method Overridden")
        pass
class CashPayment(Payment):
    def pay(self,amount):
        self.amount=amount
        print(f"{self.amount} paid in cash")
class CardPayment(Payment):
    def pay(self,amount):
        self.amount=amount
        print(f"{self.amount} paid using card")
class UPIPayment(Payment):
    def pay(self,amount):
        self.amount=amount
        print(f"{self.amount} paid using UPI")
payments=[CashPayment(),CardPayment(),UPIPayment()]
for i in payments:
    i.pay(1000)