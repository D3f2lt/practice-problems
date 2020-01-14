ls = [9,3,9,3,9,7,9]

def solution(A):
    for e in ls:
        count = ls.count(e)
        if count == 1:
            return e

if __name__ == "__main__":
    print(solution(ls))
