
def solution(A, K):
    """
        A represent list/array
        K an integer that represent rotation of the list K times
          if K is negative that means rotation to right, if 
    """
    return A[K:]+A[:K]

if __name__ == "__main__":
    print(solution([1,2,3,4,5], -3))
