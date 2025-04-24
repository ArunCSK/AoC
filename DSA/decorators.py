class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2
    
    @property
    def constants(self):
        return 3.14159 
    

    


circle = Circle(5)
print(circle.area)  # Output: 78.53975
print(circle.constants)