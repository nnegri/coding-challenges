# BFS
# #take node[0]
# #if match, return
# #else, append children
def bfs(root, node):
    search_lst = [root]
    found = False
    while search_lst:
        curr = search_lst.pop(0)
        if curr.data == node.data:
            return curr
        else:
            search_lst.extend(curr.children)
    return "Not Found"

# DFS
# #take last node
# #if match, return
# #else, append children
def dfs(root, node):
    search_lst = [root]
    found = False
    while search_lst:
        curr = search_lst.pop()
        if curr.data == node.data:
            return curr
        else:
            search_lst.extend(curr.children)            
    return "Not Found"

# BFTraversal
# #if children, append
# #for each child, recurse
def bft(node, node_lst=None):
    if node_lst == None:
        node_lst = [node]
    if node.children:
        for child in node.children:
            node_lst.append(child)
            bft(child, node_lst)
    return node_lst

# DFTraversal
# #if node
# #recurse on left child
# #append node
# #recurse on right child
def dft(node, node_lst=None):
    if node_lst == None:
        node_lst = []
    if node != None:
        dft(node.left, node_lst)
        node_lst.append(node)
        dft(node.right,node_lst)
    return node_lst



# Mergesort
#if given len(list) is > 1
#split, recurse left and recurse right
#keep counters for left, right, list
#while we haven't reached the end of r or l, add the lesser num to list
#once we reach the end of r or l, loop through remainder of r/l and add each to list
def mergesort(lst):
    if len(lst) > 1:
        mid = len(lst) / 2
        left = lst[:mid]
        right = lst[mid:]

        mergesort(left)
        mergesort(right)

        l = 0
        r = 0
        m = 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                lst[m] = left[l]
                l += 1
            else:
                lst[m] = right[r]
                r += 1
            m += 1
        while l < len(left):
            lst[m] = left[l]
            l += 1
            m += 1
        while r < len(right):
            lst[m] = right[r]
            r += 1
            m += 1

    return lst

print mergesort([4,7,2,6,9,1])

# RPS
#initialize list of combos
#get all possible combinations:
#for each move, for each combo create new combo with move, and append
#recurse until 3 turns
#return combinations with len of 3 exactly
def rps(moves_lst, turns=0, combos=None):
    if combos == None:
        combos = [[move] for move in moves_lst]
        turns += 1

    while turns != 3:
        for move in moves_lst:
            combo_copy = combos[:]
            for combo in combo_copy:
                new_combo = combo + [move]
                combos.append(new_combo)
        turns += 1
        return rps(moves_lst, turns, combos)

    return [combo for combo in combos if len(combo) == 3]

print rps(['r','p','s'])




