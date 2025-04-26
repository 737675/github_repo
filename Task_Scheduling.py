#Task Scheduling Problem 

import heapq

def max_tasks(tasks):
    tasks.sort(key=lambda x: x['deadline'])  # Step 1: Sort by deadline
    total_time = 0
    max_heap = []

    for task in tasks:
        heapq.heappush(max_heap, -task['duration'])  # use negative to simulate max heap
        total_time += task['duration']

        if total_time > task['deadline']:
            removed = heapq.heappop(max_heap)
            total_time += removed  # remove longest duration task

    return len(max_heap)

#Example Input
tasks = [
    {'name': 'Task 1', 'deadline': 4, 'duration': 2},
    {'name': 'Task 2', 'deadline': 3, 'duration': 1},
    {'name': 'Task 3', 'deadline': 2, 'duration': 1},
    {'name': 'Task 4', 'deadline': 1, 'duration': 2},
]
print("Maxium tasks that can be Completed:", max_tasks(tasks))
