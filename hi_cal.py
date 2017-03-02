def hi_cal(times):
    times.sort()
    return_times = []
    merged = False

    if times[0][1] == max([times[i][1] for i in range(len(times))]):
        return_times.append(times[0])
    else:

        for i in range(len(times)-1):
            if merged == True:
                merged = False
                continue
            if times[i][0] < times[i+1][0] and times[i][1] >= times[i+1][0] and times[i][1] < times[i+1][1]:
                return_times.append((times[i][0], times[i+1][1]))
                merged = True
            else:
                return_times.append(times[i])

    return return_times


print hi_cal([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
print hi_cal([(1, 2), (2, 3)])
print hi_cal([(1, 5), (2, 3)])
print hi_cal([(1, 10), (2, 6), (3, 5), (7, 9)])


def merge_ranges(meetings):

# sort by start times
    sorted_meetings = sorted(meetings)

    # initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:

        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # if the current and last meetings overlap, use the latest end time
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))

        # add the current meeting since it doesn't overlap
        else:
            merged_meetings.append((current_meeting_start, current_meeting_end))


    return merged_meetings

print merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])