sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12),
            (9, 10), (10, 11), (10, 12), (11, 12)]

def bestTimeToParty(schedule):
    # Find start time and end time
    start = schedule[0][0]
    end = schedule[0][1]
    
    for c in schedule:
        start = min(c[0], start)
        end = max(c[1], end)
    print(start, end)

    count = celebrityDensity(schedule, start, end)

bestTimeToParty(sched)


