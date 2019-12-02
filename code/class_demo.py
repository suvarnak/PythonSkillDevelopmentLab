
from math import *

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def distance_from_origin(self):
		return sqrt(self.x * self.x + self.y * self.y)
	
	def distance(self, other):
		dx = self.x - other.x
		dy = self.y - other.y
		return sqrt(dx * dx + dy * dy)


a_point = Point(3, 4)
print(a_point.distance_from_origin())

another_point = Point(6, 4)
a_point.distance(another_point)
