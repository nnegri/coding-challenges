
def phone_combos(phone_numbers, digit_dict, combinations=None):

    if combinations == None:
        combinations = [ch for ch in digit_dict[phone_numbers[0]]]
    if phone_numbers:
        temp_comb = combinations[:]
        for ch in digit_dict[phone_numbers[0]]:
            for word in temp_comb:
                word += ch
                combinations.append(word)

        return phone_combos(phone_numbers[1:], digit_dict, combinations)

    return combinations

print phone_combos("123", {"1":['a','b','c'], "2":['d','e','f'], "3":['g','h','i']})