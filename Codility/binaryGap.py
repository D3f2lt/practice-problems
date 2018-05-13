import time

def binary_gap(N):
    """Solution to binary gap"""
    current_gap = 0
    max_gap = 0

    ## since even integer have this uniqe representation.
    ## this while loop eliminate the trailing zero
    ## that is not surrounded by ones at both end
    ## in the binary repesentation of N.
    while N > 0 and N % 2 == 0:
        N = N/2
        
    while N > 0:
        bin_x = N%2
        if bin_x == 1:
            max_gap = max(max_gap, current_gap)
            current_gap = 0
        else:
            current_gap += 1
        N = N//2

    return max_gap


t0=time.time()
##print binary_gap(20)
##print binary_gap(2147483647)
t1=time.time()
print 'time required = ', t1-t0
