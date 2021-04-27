from collections import Counter

def sockMerchant(n, ar):

    noOfPairs = 0
    for element in set(ar):
        noOfPairs += ar.count(element) // 2
    print(noOfPairs)

ar = [1,2,1,2,3,2,1,2]
sockMerchant(8,ar)
