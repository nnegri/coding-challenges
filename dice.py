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