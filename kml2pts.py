# kml2pts.py
# Extracts geographic points from a kml file
# Brendan Hasz
# winsto99@gmail.com

import string as s
import sys
import matplotlib.pyplot as plt
import numpy as np

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


# TESTER
fname_IN = sys.argv[1]
print "Extracting points from "+fname_IN
blocks = kml2pts(fname_IN)
print "Done!"

# TEST BY PLOTTING
x = [e[0] for e in blocks[0]]
y = [e[1] for e in blocks[0]]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
ax.set_aspect('equal')
plt.title('A kml path')
plt.show()

