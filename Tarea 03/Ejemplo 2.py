# ============================================
# Programación Orientada a Objetos (POO)
# Ejemplo: Gestión de una cuenta bancaria
# ============================================

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = 0

    def deposit(self, amount):
        self.balance += amount
        self.transactions += 1
        print("Deposit:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions += 1
            print("Withdraw:", amount)
        else:
            print("Not enough balance to withdraw.")

# Crear una instancia de la clase BankAccount
account = BankAccount()

# Uso de los métodos en la programación orientada a objetos
account.deposit(500)
account.withdraw(200)

# Imprimir el estado final de la cuenta
print("Balance (OOP):", account.balance)
print("Transactions (OOP):", account.transactions)
