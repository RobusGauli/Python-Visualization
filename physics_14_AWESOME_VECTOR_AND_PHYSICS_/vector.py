from math import sin, cos, hypot, pow, sqrt, atan
class Vector(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return Vector(self.x, self.y)
        
    def __abs__(self):
        #return the magnitude of the vector 
        a = pow(self.x, 2)
        b = pow(self.y, 2)
        return sqrt(a+b)
    
    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return Vector(self.x, self.y)
        
    def __mul__(self, scalar):
        self.x = self.x * scalar
        self.y = self.y * scalar
        return Vector(self.x, self.y)
    
    def __div__(self, scalar):
        self.x = self.x / scalar
        self.y = self.y / scalar
        return Vector(self.x, self.y)
    
        
    #normalization of vector
    def norm(self):
        magnitude = abs(self)
        #if magnitude is more than 0
        if magnitude > 0 :
            self.x = self.x / magnitude
            self.y = self.y / magnitude
            return Vector(self.x, self.y)
        return 'Magnitude of vector is Zero so cannot get the normalization'
    
 
    def direction(self):
        ''' Find the direction of the vector'''
        
        if self.y > 0:
            a = self.x / self.y
            return atan(a)
        return 'Value of y is 0'
    
    @staticmethod
    def fromAngle(angle):
        '''return the unit vector from the given angle'''
        
        x = cos(angle)
        y = sin(angle)
        #unit vector with the direction 
        return Vector(x, y)
    
        
 
           
        
        
    def __str__(self):
        return 'Vector {0} {1}'.format(self.x, self.y)
    
    