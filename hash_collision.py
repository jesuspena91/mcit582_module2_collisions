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
import binascii

def random_numbers():
    random_base = int(math.pow(255, 3)) # As a rule though, you’ll have to make sure that 255^(x) is greater than 2^k

    random_num_x = os.urandom(random_base)
    random_num_y = os.urandom(random_base)
    x = hashlib.sha256(random_num_x).hexdigest().encode('utf-8')
    y = hashlib.sha256(random_num_y).hexdigest().encode('utf-8')

    return (x, y)

def hash_collision(k): # The largest instance the autograder will test on is k=20.
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
   
    #Collision finding code goes here
    x, y = random_numbers()
    
    while True:
        x, y = random_numbers()
        if (x[-k:] == y[-k:]):
            break
    
    print(x)
    print(y)
    
    return(x, y)

hash_collision(1)