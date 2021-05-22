# Use a brute-force algorithm to find a partial collision
# Using the template “hash_collision.py” write a function called “hash_collision” that takes a single input, k, 
# where k is an integer. The function “hash_collision” should return two variables, x and y, 
# such that that the SHA256(x) and SHA256(y) match on their final k bits. The return variables, x and y, 
# should be encoded as bytes.
# Your algorithm should be randomized, i.e., hash_collision(k) should not always return the same colliding pair.

# To encode a string as bytes
# str = "Hello World"
# byte_str = str.encode('utf-8')

# Return a string of size random bytes suitable for cryptographic use
# os.urandom(size)
# x = b'\x00'
# y = b'\x00'

# L = [hashlib.sha256(x.encode('utf-8')).hexdigest() for x in M]

import hashlib
import os
import math

def hash_collision(k): # The largest instance the autograder will test on is k=20.
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
    
    random_base = 1048577 # As a rule though, you’ll have to make sure that 255^(x) is greater than 2^k
    x = os.urandom(random_base)
    #Collision finding code goes here
    while True:
        y = os.urandom(random_base)

        hash_x = hashlib.sha256(x).hexdigest()
        int_x = int(hash_x, base=16)
        binary_x = str(bin(int_x))[2:]

        hash_y = hashlib.sha256(y).hexdigest()
        int_y = int(hash_y, base=16)
        binary_y = str(bin(int_y))[2:]

        if (binary_x[-k:] == binary_y[-k:] and x != y):
            break

    #print(binary_x)
    #print(binary_y)

    return(str(x).encode('utf-8'), str(y).encode('utf-8'))

#hash_collision(20)