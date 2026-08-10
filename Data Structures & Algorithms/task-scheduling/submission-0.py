import string
import heapq
from collections import deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_to_index = {task: index for index, task in enumerate(string.ascii_uppercase)}

        # Step 1: Count the frequency of each task
        task_counts = [0] * 26
        for task in tasks:
            task_counts[task_to_index[task]] += 1

        # Step 2: Max heap (we use negative counts to simulate a max-heap using heapq which is min-heap by default)
        max_heap = []
        for i in range(26):
            if task_counts[i] > 0:
                heapq.heappush(max_heap, (-task_counts[i], i))  # Store negative to simulate max-heap

        # Step 3: Queue for cooling down tasks
        queue = deque()
        time = 0

        while max_heap or queue:
            time += 1

            # Step 4: Process tasks
            if max_heap:
                # Get the task with the highest frequency
                count, task_index = heapq.heappop(max_heap)
                count = -count  # Convert back to positive count

                # Decrease the task's count
                count -= 1

                if count > 0:
                    # Put task in cooldown queue with the time it can reenter heap
                    queue.append((task_index, count, time + n))

            # Step 5: Check and add tasks back to heap after cooldown
            if queue and queue[0][2] <= time:
                task_index, count, _ = queue.popleft()
                heapq.heappush(max_heap, (-count, task_index))

        return time
