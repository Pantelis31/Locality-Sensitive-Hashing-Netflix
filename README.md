## Locality-Sensitive-Hashing

This project is an implementation of the Locality-Sensitive-Hashing (LSH) algorithm with minhashing, for the Netflix Prize dataset which can be found [here](https://surfdrive.surf.nl/files/index.php/s/WwZqzkkHxg6KLlL
). By creating a signature matrix, the Jaccard similarities between pairs of users can be computed. Therefore, one can identify users with high similarity based on the movies they have watched.

* **sig.py** contains the script which generates the signature matrix, for which we can compute the Jaccard similarities.
* **sig.zip** contains the signature matrix.
* **utils.py** contains the utility functions including the LSH algorithm function.
* **run.py** performs the LSH algorithm.
* **ans.txt** contains an example output of the LSH function.

### The following tools were used: 
 
* numpy 
* itertools
* scipy 