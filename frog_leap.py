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
    out = [-1]*x

    for i in range(len(A)):
        if out[A[i]-1] == -1 or i < out[A[i]-1]:
            out[A[i]-1] = i

    if -1 in out:
        return -1
    else:
        return max(out)

print alt_frog_leap(5, [1,3,1,4,2,3,5,4])
print alt_frog_leap(5, [2,4,5,3,3,4,2])


