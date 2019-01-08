#We are going to create a method that allows us to move a point to an arbitrary position
import math #import the module math

#define your class
class Point:
    def move(self, x, y): #define your method
        self.x = x
        self.y = y

    def reset(self): #moves the value of x to 0 and y to 0
        self.move(0,0)

    def calculate_distance(self, other_point): #calculates the distance between point and other_point
        return math.sqrt(
            (self.x - other_point.x)**2 +
            (self.y - other_point.y)**2
        )
