def activity_selection(activities):
    # activities: list of tuples (start, finish)
    # Sort activities by finish time
    activities.sort(key=lambda x: x[1])
    n = len(activities)
    selected = []

    # The first activity always gets selected
    if n == 0:
        return selected
    selected.append(activities[0])
    last_finish = activities[0][1]

    for i in range(1, n):
        if activities[i][0] >= last_finish:
            selected.append(activities[i])
            last_finish = activities[i][1]
    return selected

# Example usage
if __name__ == "__main__":
    # Each activity is represented as (start_time, finish_time)
    activities = [(1, 3), (2, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
    selected_activities = activity_selection(activities)
    print("Selected activities:")
    for act in selected_activities:
        print(f"Start: {act[0]}, Finish: {act[1]}")


# def activity_selection(activities):
#     activities.sort(lambda x: x[1])
#     n = len(activities)
#     selected = []
    
#     if n == 0:
#         return selected
#     selected.append(activities[0])
#     last_finish = activities[0][1]

#     for i in range(1,n):
#         if activities[i][0] >= last_finish:
#             selected.append(activities[i])
#             last_finish = activities[i][1]
#     return selected

# if __name__ == "__main__":
#     activities = [()]
#     selected_activities = activity_selection(activities):
#     print("Selected activities: ")
#     for act in selected



## LEARNINGS:
# lambda function
# its use in sort and filter inbuilt methods 

# list operation append()... what about remove and swaps?



def activity_selection(activities):
    activities.sort(lambda x: x[1])

    n = len(activities)
    selected = []
    last_finish = activities[0][1]

    if (n==0):
        return selected
    for i in range(1,n):
        if (activities[i][0] >= last_finish):
            selected.append(activities[i])
            last_finish = activities[i][1]
    return selected

if __name__ == "__main__":
    activities = [] 
    # fill this list with pair tuples of start and end times

    selected_activites = activity_selection(activities)
    # result 

    # print the result
