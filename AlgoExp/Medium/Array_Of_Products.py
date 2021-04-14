# Time - O(n^2)
# Space - O(n)
def arrayOfProducts(array):
    # Write your code here.
    out = []
    i = 0
    while i < len(array):
        prod = 1
        for j in range(len(array)):
            if j != i:
                prod *= array[j]
        out.append(prod)
        i += 1
    return out

# Time - O(3n) -> O(n)
# Space - O(3n) --> O(n)
def arrayOfProductsGiven(array):
    # Write your code here.
    leftProd = [1 for _ in range(len(array))]
    rightProd = [1 for _ in range(len(array))]
    out = []
        
    # calculate all products to the left of current value
    leftRun = 1
    for i in range(len(array)):
            leftProd[i] = leftRun
            leftRun *= array[i]
            
    # calculate all products to the right of the current value
    rightRun = 1
    for i in reversed(range(len(array))):
            rightProd[i] = rightRun
            rightRun *= array[i]
    
    # calculat the products of the two arrays and return
    for i in range(len(array)):
            out.append(leftProd[i] * rightProd[i])
    return out