#///////////////////////////////////////////////////////////////////
# Project: Bitcoin Explained (Voltara)
# By Raafay Tariq
#
# The purpose of this project is to go through the steps of SHA-256
# one by one and execute them in Python 3.6. this is a test build just
# to prove the viabillity of executing the project on a backend
#///////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////////
# Step 0. We declare the global variables and import the needed
# Packages.
#///////////////////////////////////////////////////////////////////
import os
import random
os.chdir('C:\\Users\\Raafay\\Desktop\\Bitcoin Explained Voltara')
#///////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////////
# Step 1. Let us first import and read the file which contains the 
# the 8 blocks we will use to execute the SHA-256 protocol.
# the blocks will be taken from file blocks.txt
#///////////////////////////////////////////////////////////////////
blocks_list = [blocks_list.rstrip('\n') for blocks_list in open('blocks.txt')]
print(blocks_list);
#///////////////////////////////////////////////////////////////////
# Step 2. We will need to convert the first,second and third (0,1,2)
# hashes into binary.
#///////////////////////////////////////////////////////////////////
# WARNING-----------------------------------------------------------
# The Below Code is just dummy code talking about how the general
# Process for the majority function. this is ideally what we connect
# with the transformation function in order to create the full
# Majority function.
#///////////////////////////////////////////////////////////////////
a = format(5, '07b')
b = format(3, '07b')
c = format(ord('e'), '07b')

print(a)
print(b)
print(c)
print(int(a) + int(b) + int(c));

#///////////////////////////////////////////////////////////////////
# Error Found, addition of bits done in integer form, not binary
#///////////////////////////////////////////////////////////////////
hash_1 = int(a) + int(b) + int(c)
hash_1 = str(hash_1);

token = [None]*len(hash_1);


for x in range(0,len(hash_1)):
    if int(hash_1[x]) >= 2:
        token[x] = '1'
    else:
        token[x] = '0'
print(token);

new_string = ''.join(token)

n = int(new_string, 2)
n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
print(n)
#///////////////////////////////////////////////////////////////////

