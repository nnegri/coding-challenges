# def word_break(s, dict):
    
#     for i in range(len(s) - 1):    
#         if s[:i] in dict:
#             return True


def number_perm(s):
    nums = [[] for i in range(len(s))]
    nums[0] = [int(s[0])]
    for i in range(1, len(s)):
        nums[0].append(int(s[i]))
        nums[i].append(int(s[:i]))
        nums[i].append(int(s[i:]))
    return nums

print number_perm("121")



def pretty_tree(node):
    output = []
    to_visit = [node]
    next_newline_ch = node
    while to_visit:
        node = to_visit.pop(0)
        # print node
        output.append(node.data)
        printed_newline = False
        if next_newline_ch == node:
            # print "\n"
            output.append("\n")
            printed_newline = True
        if node.children:
            to_visit.extend(node.children)
        if printed_newline and to_visit:
            next_newline_ch = to_visit[-1]
    return " ".join(output)
        


def k_smallest(k, node, elements=None):

    if elements == None:
        elements = []
    if node != None:
        if node.left:
            k_smallest(k, node.left, elements)
        elements.append(node)
        if node.right:
            k_smallest(k, node.right, elements)
    return elements[k-1]


def match_str(s, pattern):

    init_combos = []
    alpha_dict = {}
    for i in range(len(pattern)-2):
        if pattern[i].isalpha():
            for j in range(1, int(pattern[i+2])+1):
                # init_combos.append([pattern[i] * j])
                if i in alpha_dict:
                    alpha_dict[i].append([pattern[i] * j])
                else:
                    alpha_dict[i] = [[pattern[i] * j]]
    
    sorted_keys = sorted(alpha_dict.keys())

    init_combos = [v for v in alpha_dict[sorted_keys[0]]]

    for key in sorted_keys[1:]:
        combos = init_combos[:]

        for v in alpha_dict[key]:
            init_combos.append(v)
            
            for combo in combos:
                new_combo = combo[0] + v[0]
                init_combos.append([new_combo])
            

    return [s] in init_combos

print match_str("aab", "a(3)b(3)")
print match_str("abc", "a(3)b(3)c(2)")



# def buffer_message(size, message):
#     i = 0
#     for word in message:
#         output[i] = []
#         while len(output[i]) + len(word) + 1 <= size:
#             output[i].append(word, " ")
#         output[i].append("(" + str(i) + "/" + )

def match_index(int_lst):
    for i in range(len(int_lst)):
        if i == int_lst[i]:
            return i
print match_index([-1, 0, 1, 2, 3, 5])

def reverse_words(sentence):

    lst = sentence.split(" ")
    i = len(lst)-2

    while i >= 0:
        word = lst.pop(i)
        lst.append(word)
        i -= 1

    return " ".join(lst)

print reverse_words("hello I am dog")


def pig_latin_encode(sentence):
    words = sentence.split(" ")
    output = ""
    for word in words:
        first_letter = word[0]
        new_word = word[1:] + first_letter + "ay"
        output += new_word + " "
    return output

print pig_latin_encode("hello there piggy")

def pig_latin_decode(sentence):
    words = sentence.split(" ")
    output = ""
    for word in words:
        first_letter = word[-3]
        new_word = first_letter + word[:-3]
        output += new_word + " "
    return output 
print pig_latin_decode("ellohay heretay iggypay")


def note_pad(n):
    if n % 3 == 0:
        i = (n - 1) / 3
    else:
        i = n/3

    max_chars = n
    max_i = 0
    while i > 0:
        x = n - i*3
        j = i
        while j > 0:
            x = x * 2
            j -= 1
        if x > max_chars:
            max_chars = x
            max_i = i
        i -= 1
    return max_chars, max_i
print note_pad(4)
print note_pad(7)
print note_pad(20)


def menu_budget(menu, budget):
    cost_dict = {}
    output = []
    for cost in menu:
        if cost in cost_dict:
            cost_dict[cost].append([cost])
        else:
            cost_dict[cost] = [[cost]]
        for other_cost in menu:
            if cost + other_cost < budget:
                if (cost + other_cost) in cost_dict:
                    cost_dict[cost + other_cost].append([cost, other_cost])
                else: 
                    cost_dict[cost + other_cost] = [[cost, other_cost]]
    
    for cost in menu:
        remainder = budget - cost
        for dollars in cost_dict[remainder]:
            dollars.append(cost)
            output.append(dollars)

    return output

print menu_budget([5,10,15], 20)
    #5 + ways to get to 15
    #10 + ways to get to 10
    #15 + ways to get to 5

# [[5,5,5,5], [5,5,10], [5,15], [10,10]]


def move_zeroes(lst):
    if not lst:
        return

    for i in range(len(lst)-1):
        if lst[i] == 0:
            j = i + 1
            swapped = False
            while swapped == False:
                if lst[j] != 0:
                    lst[i] = lst[j]
                    lst[j] = 0
                    swapped = True
                else:
                    j += 1
                if j == len(lst):
                    return lst 



    # right_pointer = len(lst) - 1

    # for left_pointer in range(len(lst)):
    #     if left_pointer > right_pointer:
    #         lst[left_pointer] = 0
    #         continue

    #     if lst[left_pointer] != 0:
    #         continue

    #     if lst[left_pointer] == lst[right_pointer]:
    #         right_pointer -= 1
        
    return lst

print move_zeroes([4,5,0,7,4,0,7,4,5])











