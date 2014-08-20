# geo-reader.py
#
# Functions for reading in geographical data files, such as gpx, kml, etc
#
# Brendan Hasz
# winsto99@gmail.com

import string as s

def gpx2pts(fname):
    '''
    Given a filename for a gpx file, this function returns a list of
    points from the gpx file
    '''
    pts = []
    with open(fname, 'r') as f:
        while True: #while we're not yet at end of file
            l = f.readline()  #read a new line
            if not l: break  #if we've reached EOF, quit
            if s.find(l,'<trkpt')!=-1: #but if this is a trkpt line,
                p = l.split('\"'); #parse the line
                pts.append([float(p[1]), float(p[3])])  #parse this line + save
    return pts 


def kml2pts(fname):
    '''
    Given a filename for a kml file, this function returns a list of
    3d points from the kml file
    '''
    blocks = []
    with open(fname, 'r') as f:
        while True: #while we're not yet at end of file
            l = f.readline()  #read a new line
            if not l: break  #if we've reached EOF, quit

            # If this is the start of a coords BLOCK (don't include single pts)
            if s.find(l,'<coordinates')!=-1 and s.find(l,'</coordinates')==-1: 
                pts = []  #array to save points for this block in
                l = f.readline()  #read next line
                while s.find(l,'</coordinates')==-1:  #while not at end of blk
                    pts.append([float(n) for n in l.strip().split(',')])  #parse this line + save
                    l = f.readline()  #read next line
                blocks.append(pts)  #add this block of points to blocks array

    return blocks
