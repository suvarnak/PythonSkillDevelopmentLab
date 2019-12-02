class bank_account:
	def __init__(self, initial_balance, account_holder):
		self.balance = initial_balance
		self.account_holder = account_holder
		
	def credit(self,credit_amount):
		self.balance = self.balance + credit_amount

	def debit(self,debit_amount):
		self.balance = self.balance - debit_amount

	def print_balance(self):
		print(self.balance)
		
	def __str__(self):
		return "The account has "+str(self.balance) +"Rs."


b = bank_account(100,"SKK")
print(b)
