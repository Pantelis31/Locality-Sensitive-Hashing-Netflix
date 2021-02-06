import numpy as np
from itertools import combinations
from scipy.sparse import csr_matrix

#load the data
data = np.load("user_movie.npy")

#Initialize the input matrix as a sparse matrix
my_matrix = csr_matrix((len(set(data[:,1])),len(set(data[:,0])) ), dtype=np.int8).toarray()
nrow = len(data)

#Fill the sparse matrix
for row in range(nrow):
    user = data[row,0] 
    movie = data[row,1] 
    my_matrix[movie,user] = 1 

np.random.seed(17)

# initialize matrix M with Inf values
M = np.full((100,len(set(data[:,0]))), np.inf)

# number of movies 
m = len(set(data[:,1]))

# next prime number after m. 
p = 17783

# Coefficients a and b
A = np.random.permutation(m)
B = np.random.permutation(m)
a = A[:100]
b = B[:100]

# Creating signature matrix
nrow = len(my_matrix)
ncol = my_matrix.shape[1]


for row in range(nrow):
    print("Row: " + str(row))
    # Compute hash functions for row
    H = (a*row + b)%p
    for col in range(ncol):
        if my_matrix[row,col] == 1 :
            for j in range(100):
                if H[j] < M[j,col] :
                    M[j,col] = H[j]
                    
#Save signature matrix                  
np.save('sig.npy', M)