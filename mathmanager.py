class mathmanager:

	def add(self, a, b):
		return a+b

	def subtract(self, a, b):
		return a-b

	def multiply(self, a, b):
		return a*b
	
	def monthly_intrest(self, amount, period):
		if amount < 0:
			raise ValueError("Amount must be a positive number")
		
		if period == 1:
			rate = 0.038
		elif period == 2:
			rate = 0.036
		else:
			raise ValueError("Invalid period, must be 1 or 2 years")

		return round(amount * (1 + (rate /12)) ** (12 * period), 2)

	def tax(self, income):
		if income < 0:
			raise ValueError("Income must be a positive number")
		
		if income <= 12570:
			rate = 0
		elif income <= 50270:
			rate = 0.2
		elif income <= 125140:
			rate = 0.4
		else:
			rate = 0.45
		
		return income * rate

	def degree_classification(self, grades):
		grades.remove(min(grades))
		average = sum(grades) / len(grades)

		if average < 40:
			return "Fail"
		elif average < 50:
			return "Third"
		elif average < 60:
			return "Second"
		elif average < 70:
			return "Upper Second"
		else:
			return "First"