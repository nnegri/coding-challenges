
def string_sort(strng):
    dicto = {}

    for ch in strng:
        dicto[ch] = dicto.get(ch, 0) + 1

    new_dict = {}
    for key in dicto.keys():
        if dicto[key] in new_dict:
            new_dict[dicto[key]].append(key)
        else:
            new_dict[dicto[key]] = [key]

    output = []
    for key in sorted(new_dict.keys(), reverse=True):
        for letter in new_dict[key]:
            output.extend(sorted(letter)*key)

    return "".join(output)

print string_sort("bbaaccc")
print string_sort("banana")


def find_min(lst):

    mid = len(lst) / 2

    while mid >= 0 or mid < len(lst):

        if lst[mid-1] > lst[mid] and lst[mid+1] > lst[mid]:
            return lst[mid]

        if lst[mid-1] < lst[mid]:
            mid -= 1

        if lst[mid+1] < lst[mid]:
            mid += 1

print find_min([5,4,3,2,1,2,3,4,5])
print find_min([5,4,3,2,3])


def find_unduplicate(lst, compare_list=None):

    if compare_list == None:
        compare_list = []

    if len(lst) == 1:
        compare_list.append(lst)

    elif len(lst) == 2 and lst[0] != lst[1]:
        compare_list.append(lst)

    if len(lst) > 2:
        mid = len(lst) / 2

        left = lst[:mid]
        right = lst[mid:]

        find_unduplicate(left, compare_list)
        find_unduplicate(right, compare_list)

    if len(compare_list) == 1:
        return compare_list[0][0]
    elif len(compare_list) == 2:
        return abs(sum(compare_list[0]) - sum(compare_list[1]))

    

print find_unduplicate([1,2,2,3,3])
print find_unduplicate([1,1,2,3,3])



def int_to_string(num):

    str_num = str(num)
    output = ""

    if len(str_num) == 1:
        output = ".0" + str_num

    elif len(str_num) == 2:
        output = "." + str_num

    else:
        i = 0
        while i+5 < len(str_num):
            if (len(str_num) - i) % 3 == 0:
                output += str_num[i] + ","
                i += 1
            elif (len(str_num) - i) % 3 == 1:
                output += str_num[i] + str_num[i+1] + ","
                i += 2
            elif (len(str_num) - i) % 3 == 2:
                output += str_num[i] + str_num[i+1] + str_num[i+2] + ","
                i += 3
        while i+2 < len(str_num):
            output += str_num[i]
            i += 1
        output += "." + str_num[-2] + str_num[-1]
        
    return output

print int_to_string(100000000)


def square_rt(num):

    i = 0
    while i*i < num:
        i += 1

    return i

print square_rt(100)


def max_profit(lst):

    min_price = lst[0]
    sell_price = lst[0]
    profit = 0

    for price in lst[1:]:
        if price - min_price > profit:
            profit = price - min_price
            sell_price = price
        if price < min_price:
            min_price = price

    return [profit, sell_price, sell_price - profit]


print max_profit([3,4,2,6,7,5,1])


def int_pairs(target, lst):

    output = []
    lst.sort()

    low = 0
    high = -1

    while low != high and low < len(lst) and high >= -len(lst):
        if lst[low] + lst[high] == target:
            output.append((lst[low], lst[high]))
            lst = lst[:low] + lst[low+1:high] + lst[high+1:]
        elif lst[low] + lst[high] < target:
            low += 1
        elif lst[low] + lst[high] > target:
            high -= 1

    return output

print int_pairs(10, [1,3,4,5,6,7,8])


def int_range(num1, num2, lst):

    if sum(lst) == int((num1 + num2) * (((abs(num1 - num2) + 1) / 2.0))):
        return True

    return False

print int_range(1,5, [2,4,5,3,1])
print int_range(1,5, [2,4,5,1])












