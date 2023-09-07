def count_ants(A, B):
    K_min = find_min(A, B)
    K_max = find_max(A, B)
    
    if find_min(A, B) == 1 and K_max == 0: # case when all ants are moving opposite direction
        return 0

    K = K_max - K_min + 1
    return K
    

def find_max(A, B):
    counter = 0
    for i in range(len(A)):
        if A[i] <= B[i]:
            counter += 1
    return counter

def find_min(A, B):
    if not A or not B:
        return 0

    max_A = A[-1]  # Get the maximum number in A

    # Check if the minimum number in B is greater than max_A
    if B[0] > max_A:
        return len(B)
    
    # Binary search for the first element in B greater than max_A
    left, right = 0, len(B) - 1
    while left <= right:
        mid = (left + right) // 2
        if B[mid] <= max_A:
            left = mid + 1
        else:
            right = mid - 1

    a = len(B) - left
    return 1 if a == 0 else a



A = [3, 8, 10, 13, 17]
B = [4, 7, 18, 19, 20]
print(count_ants(A, B)) # Given case


A = [1,2,3,4,5]
B = [6,7,8,9,10]
print(count_ants(A, B)) # All ants going in the same direction, 1 possible value of K


A = [6,7,8,9,10]
B = [1,2,3,4,5]
print(count_ants(A, B)) # All ants going in wrong same direction, 0 possible values of K