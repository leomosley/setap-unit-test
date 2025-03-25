import unittest
from mathmanager import mathmanager

class mathmanagertest(unittest.TestCase):
	def testAdd(self):
		math = mathmanager()
		self.assertEqual(math.add(0, 3), 3)

	def testSubtract(self):
		math = mathmanager()
		self.assertEqual(math.subtract(0, 3), -3)

	def testMultiply(self):
		math = mathmanager()
		self.assertEqual(math.multiply(0, 3), 0)

	def testMonthlyIntrest(self):
		math = mathmanager()
		self.assertEqual(math.monthly_intrest(1000, 1), 1038.00)
		self.assertEqual(math.monthly_intrest(1000, 2), 1073.296)
	
	def testTax(self):
		math = mathmanager()
		self.assertEqual(math.tax(12570), 0)
		self.assertEqual(math.tax(50270), 10054)
		self.assertEqual(math.tax(125140), 50056)
	
	def testDegreeClassification(self):
		math = mathmanager()
		self.assertEqual(math.degree_classification([40, 50, 60, 70, 80]), "Upper Second")
		self.assertEqual(math.degree_classification([40, 50, 60, 70]), "Upper Second")
		self.assertEqual(math.degree_classification([40, 50, 60]), "Second")