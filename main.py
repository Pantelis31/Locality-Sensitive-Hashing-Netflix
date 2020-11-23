#########################################################
#                                                       #
#     Loading the modules and data.                    
#                                                       #
#########################################################

import numpy as np
from itertools import combinations
from scipy.sparse import csr_matrix

data = np.load("user_movie.npy")


#########################################################
#                                                       #
#   Creating the input matrix                    
#                                                       #
#########################################################

#The input matrix will be a sparse matrix with dimensions : Movies X Users
#Initialize the input matrix with zeros.
my_matrix = csr_matrix((len(set(data[:,1])),len(set(data[:,0])) ), dtype=np.int8).toarray()
nrow = len(data)

#Go through every row of the original data and create the input matrix
for row in range(nrow):
    user = data[row,0] 
    movie = data[row,1] 
    my_matrix[movie,user] = 1 

#########################################################
#                                                       #
#   Performing LSH to find similar pairs of users.                    
#                                                       #
#########################################################




# bucket_array
def bucket_array_ (bands, k) :
    bucket_array = []
    for band in range(bands):
        bucket_array.append([[] for i in range(k)])
    return bucket_array




# _hash_
def _hash_ (x):
    global nbuckets
    return int(sum(x) % nbuckets )


# load signature matrix 
M = np.load("sig.npy")

#Initialize answer file
file = open("ans.txt","w")
file.write("User1   User2   Similarity")
file.close()

# LSH function
def LSH (bands, rows, k):
    global nbuckets
    nbuckets = k
    i = 0
    pairs = set()
    bucket_array = bucket_array_(bands, k)

    for b in range(bands):
        #print("BAND: " + str(b))
        buckets = bucket_array[b]
        band = M[i:(i+rows), :]
        
        hashvalues = np.apply_along_axis(_hash_ , 0 , band)
        hash_set = set(hashvalues)
        hash_length = len(hashvalues)
        
        for value in hash_set :
            columns = list(filter(lambda x: hashvalues[x] == value, range(hash_length))) 
            buckets[value].extend(columns)
            
        i += rows
        
        for bucket in buckets :
            #print("Bucket: " + str(bucket))
            if len(bucket) > 1 :
                for comb in combinations(bucket,2):
                    A = M[:,comb[0]]
                    B = M[:,comb[1]]
                    pair = frozenset((comb[0],comb[1]))
                    agree = np.equal(A,B)
                    similarity = sum(agree)/100
                    if similarity > 0.5 and (pair not in pairs):
                        pairs.add(pair)
                        print(str(len(pairs)) + " pairs found !")
                        file = open("ans.txt","a")
                        file.writelines("\n" + str(comb[0]) + ", " + str(comb[1]) + ", " + str(similarity))
                        file.close()
                

LSH(20,5,103723)