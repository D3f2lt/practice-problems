from math import ceil

def solution(X, Y, D):
    """
       All arguments are an integers that represent:
       X current location
       Y destination location
       D fixed distance of a jump
    """
    if X <= Y:
        return ceil((Y - X) / D)


if __name__ == "__main__":
    print(solution(10, 85, 30))

