class Circle:
	def __init__(self, radius):
		self.radius = float(radius)
		self.PI = 3.13159
	
	def setRadius(self, radius):
		self.radius = radius
	
	def getRadius(self):
		return self.radius

	def getArea(self):
		return self.PI * self.radius * self.radius

	def getDiameter(self):
		return self.radius * 2
	
	def getCircumference(self):
		return 2 * self.PI * self.radius

radius = input("radius: ")
c = Circle(radius)
print(c.getRadius(), c.getArea(), c.getDiameter(), c.getCircumference())
