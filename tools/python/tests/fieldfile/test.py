#!/usr/bin/env python2.7

from pscf.fieldfile import FieldFile

print "Reading file 'rho'"
thing = FieldFile('rho')
print "Writing 'out1'"
file = open('out1','w')
thing.write(file,1,0)
#print "Reading 'out1'"
#file = open('out1','r')
#thing2 = OutFile('out1')
#print "Writing 'out2'"
#file = open('out2','w')
#thing2.write(file,1,0)

#print "\nTesting eval method (expression evaluation):\n"
#expr = 'block_length[0][0]+block_length[0][1]'
#print expr + ' = ' + str(thing.eval(expr))
