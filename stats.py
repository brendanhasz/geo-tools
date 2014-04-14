# stats.py
# Functions for calculating statistics of paths and polygons
# Brendan Hasz
# winsto99@gmail.com
# April 2014

# TODO: have to convert lat + long to miles: 
#           one deg of lat = 69.1 mi
#           one deg of long = 53 mi

from math import sqrt

def area(points):
    '''
    Finds the area of a polygon
    Input is a list of points (which are lists of x,y coords)
    Returns the area of the polygon
    '''
    def integrate(a, b):
        '''
        Integrates the line segement connecting p1 and p2
        '''
        return 0.5*(a[1]+b[1])*(b[0]-a[0])
    s = 0.0
    for i in range(1, len(points)):
        s += integrate(points[i-1], points[i])
    s += integrate(points[-1], points[0]) #add the last segment
    return s


def perimeter(points):
    '''
    Finds the perimeter of a polygon
    Input is a list of points (which are lists of x,y coords)
    Returns the perimeter of the polygon
    '''
    def pythag(a, b):
        '''
        Calculates the distance between 2 points using the 
        pythagorean theorem
        '''
        return sqrt(pow(abs(a[0]-b[0]),2)+pow(abs(a[1]-b[1]),2))
    s = 0.0
    for i in range(1, len(points)):
        s += pythag(points[i-1], points[i])
    s += pythag(points[-1], points[0]) #add the last segment
    return s


def length(points):
    '''
    Finds the length of a path
    '''
    def pythag(a, b):
        '''
        Calculates the distance between 2 points using the 
        pythagorean theorem
        '''
        return sqrt(pow(abs(a[0]-b[0]),2)+pow(abs(a[1]-b[1]),2))
    s = 0.0
    for i in range(1, len(points)):
        s += pythag(points[i-1], points[i])
    return s
