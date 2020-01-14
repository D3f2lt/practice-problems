
def solution(A):
    """
       A is a list object
    """
    len_ls = len(A) + 1
    expect_sum = len_ls * (1+len_ls)//2
    current_sum = sum(A)
    return expect_sum - current_sum


if __name__ == "__main__":
    print(solution([4,2,3,5]))
