

def rock_paper_scissors(moves_lst, output=None, turns=0):
    if output == None:
        output = [[move] for move in moves_lst]
        turns += 1
    if turns != 3:
        output_copy = output[:]
        for move in moves_lst:
            for item in output_copy:
                new_item = item + [move]
                output.append(new_item)
        turns += 1
        return rock_paper_scissors(moves_lst, output, turns)
    else: 
        return [combo for combo in output if len(combo) == 3]

print rock_paper_scissors(['r','p','s'])