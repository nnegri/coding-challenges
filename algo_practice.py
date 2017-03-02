# Given two sorted arrays, make a "zig-zag array" that consists of the highest 
# value of the two arrays, followed by the lowest, followed by the second-highest, 
# then second-lowest, etc.

def zigzag(lst, lst2, zz_array=None):
    if zz_array == None:
        zz_array = []
    
    if lst and lst2:
        if lst[-1] > lst2[-1]:
            high_num = lst.pop()
        else:
            high_num = lst2.pop()
        zz_array.append(high_num)
        if not lst2 or lst[0] < lst2[0]:
            low_num = lst.pop(0)
        elif lst2:
            low_num = lst2.pop(0)
        zz_array.append(low_num)

        return zigzag(lst, lst2, zz_array)

    return zz_array

print zigzag([1,2,3], [4,5,6])


# Triangular number: return level [0,1,3,6,10,15,21...]
#                                 [0,1, 1+2, 1+2+3, 1+2+3+4...]

def triangular(tri_number):
    total = 0
    i = 0
    while total != tri_number:
        i += 1
        total += i

    return i

print triangular(21)


# compress strings such as "aaabbbcccc" into the string "a3b3c4"  

def compress_strings(uncompressed):
    compressed = ""
    counter = 1
    for i in range(len(uncompressed)-1):
        if uncompressed[i+1] == uncompressed[i]:
            counter += 1
        else:
            compressed += uncompressed[i] + str(counter)
            counter = 1
    compressed += uncompressed[i] + str(counter)
    return compressed

print compress_strings("aaabbbcccc")


# prime factorization: 24 > 2,3,2,2

def is_not_prime(num):
    if num == 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return True
    return False

def prime_factorization(num, factors=None):
    if factors == None:
        factors = []
    for i in range(2, num+1):
        if num % i == 0:
            factors.append(i)
            factors.append(num / i)
            break
    for factor in factors:
        if is_not_prime(factor):
            factors.remove(factor)
            return prime_factorization(factor, factors)
    return factors
print prime_factorization(24)



#  closest number input : len = 5; s   = " 1, 2, 4, 5, 6" output: find the closest 
# number pair, if have many, print all of these pair, use space to print. 
# sort first, and then calculate abs, traverse to find the closest pair.

def closest_pair(lst):
    lst.sort()
    min_diff = lst[1] - lst[0]
    num1 = lst[0]
    num2 = lst[1]
    for i in range(1, len(lst)-1):
        if lst[i+1] - lst[i] < min_diff:
            num1 = lst[i]
            num2 = lst[i+1]
            min_diff = num2 - num1
    return min_diff, num2, num1

print closest_pair([4,2,7,10,8])

# 2D BFS

def twoD_bfs(self, data):
    counter = 0
    to_visit = [self]
    while to_visit:
        counter += 1
        current = to_visit.pop(0)
        if current.data == data:
            return current, counter
        to_visit.extend(current.children)

#  Make a simple web crawler to find all URLs reachable from a   given URL.
# Basically graph traversal, BFS/DFS.

def web_crawler(url, all_urls=None):
    if all_urls == None:
        all_urls = [url]
    if url.children:
        all_urls.extend(url.children)
        for child in url.children:
            return web_crawler(child, all_urls)
    return all_urls

