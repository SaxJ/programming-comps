ret = []
def printSequencesRecur(arr, n, k, index): 
    if (k == 0): 
        ret.append(arr)
  
    if (k > 0): 
        for i in range(1, n + 1):  
            arr[index] = i;  
            printSequencesRecur(arr, n, k - 1, 
                                    index + 1);  
  

def printSequences(n, k):  
    arr = list(range(n))
    printSequencesRecur(arr, n, k, 0);  
  
    return; 
  
# Driver Code 
n = 50;  
k = 25;  
printSequences(n, k);  
  
print(ret)
# This code is contributed mits 
