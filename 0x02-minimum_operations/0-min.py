#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 6
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 18
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 620
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

#n = 972
#print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))


#n = 1917030
#print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 100000000
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

