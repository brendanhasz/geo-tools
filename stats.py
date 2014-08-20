# stats.py
#
# Functions for calculating statistics of paths and polygons
#
# Brendan Hasz
# winsto99@gmail.com
# April 2014

# TODO: have to convert lat + long to miles: 
#           one deg of lat = 69.1 mi
#           one deg of long = 53 mi
# but depends on lat + long?
# see http://www.movable-type.co.uk/scripts/latlong.html

from math import sqrt

def elevation(lat, lng):
    '''
    Returns the elevation at specified lat and longitude
    '''
    def grep(lines, word):
        ''' Returns only lines containing word '''
        wordlines = []
        for l in lines:
            if word in l:
                wordlines.append(l)
        return wordlines
    def substring(string, a, b):
        ''' Returns string from end of substr a to start of substr b '''
        bind = string.find(a)+len(a)
        eind = string.find(b)
        return string[bind:eind].strip()
    import urllib2
    if not isinstance(lat, basestring):
        lat = str(lat)
    if not isinstance(lng, basestring):
        lng = str(lng)
    reqstr = "http://maps.googleapis.com/maps/api/elevation/json?locations="
    resp = urllib2.urlopen(reqstr+lat+','+lng).read().split('\n') #read google elevation api response
    eleline = grep(resp, "elevation")[0] #find the elevation line
    return float(substring(eleline, ": ", ',')) #extract the elevation


def havdist(a, b):
    '''
    Calculates the distance (in mi) between two [lat, lon] pairs
    '''
    #R = 

def area(points):
    '''
    Finds the area of a polygon
    Input is a list of points (which are lists of x,y coords)
    Returns the area of the polygon
    '''
    #TODO: CONVERT TO MILES (OR SOMETHING?)
    def integrate(a, b):
        '''
        Integrates the line segement connecting p1 and p2
        '''
        return 0.5*(a[1]+b[1])*(b[0]-a[0])
    s = 0.0
    for i in range(1, len(points)):
        s += integrate(points[i-1], points[i])
    s += integrate(points[-1], points[0]) #add the last segment
    if s < 0:
        return area([points[-i] for i in range(1,len(points))])
    else:
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
