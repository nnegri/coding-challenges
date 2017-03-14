def frog_leap(x, A):
    jump_dict = {}

    for i in range(0, len(A)):
        if A[i] not in jump_dict and A[i] <= x:
            jump_dict[A[i]] = i

    if len(jump_dict) < x:
        return -1
    return max(jump_dict.values())

print frog_leap(5, [1,3,1,4,2,3,5,4])
print frog_leap(5, [2,4,5,3,3,4,2])

def alt_frog_leap(x, A):
    out = [-1]*x # create array to store seconds it takes each leaf to fall; -1 will indicate the leaf has not fallen

    for i in range(len(A)): #loop through each second for which a leaf falls
        #if we have not encountered leaf that falls at second i or if we encounter the same leaf that falls earlier
        if out[A[i]-1] == -1 or i < out[A[i]-1]:
            #assign i seconds to position in out corresponding to leaf
            out[A[i]-1] = i

    if -1 in out: #if not all leaves fall
        return -1
    else:
        return max(out) #return latest frog can leap

print alt_frog_leap(5, [1,3,1,4,2,3,5,4])
print alt_frog_leap(5, [2,4,5,3,3,4,2])


