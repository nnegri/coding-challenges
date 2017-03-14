def two_dice(dice1, dice2):

    output = []

    for num in dice1:
        for num2 in dice2:
            output.append(num+num2)

    count = 0
    for total in output:
        if total >= 11:
            count += 1

    return (count/float(len(output)))*100

print two_dice([1,2,3,4,5,6], [1,2,3,4,5,6])




def sum_of_pairs(lst):
    total = 0
    for item in lst:
        total += item*(len(lst)-1)

    return total

print sum_of_pairs([1,2,3,4])


def sum_to_ten(lst):

    for i in range(len(lst)-2):

        left = i + 1
        right = len(lst)-1

        while left < right:
            if lst[i] + lst[left] + lst[right] == 10:
                return [lst[i], lst[left], lst[right]]

            elif lst[i] + lst[left] + lst[right] < 10:
                left += 1

            elif lst[i] + lst[left] + lst[right] > 10:
                right -= 1

    return "None found"


print sum_to_ten([1,2,3,4,5])
print sum_to_ten([1,2,3,4])


# def k_smallest_array(lst, k):
#         smallest = lst[0]
#     for num in lst[1:]:
#         if num < smallest:
#             smallest = num
#         else:
            






