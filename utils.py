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


# LSH algorithm
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