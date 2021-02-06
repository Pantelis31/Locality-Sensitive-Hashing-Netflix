
#########################################################
#                                                       #
#   Performing LSH to find similar pairs of users.                    
#                                                       #
#########################################################

import numpy as np
from itertools import combinations
from utils import bucket_array_, _hash_, LSH

# load signature matrix 
M = np.load("sig.npy")

#Initialize answer file
file = open("ans.txt","w")
file.write("User1   User2   Similarity")
file.close()

#Run the algoithm
LSH(20,5,103723)