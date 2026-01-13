class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        # Sort tasks by end time
        tasks.sort(key=lambda x: x[1])
        
        # Track which time slots are used (up to 2000)
        max_time = max(task[1] for task in tasks)
        used = [False] * (max_time + 1)
        
        for start, end, duration in tasks:
            # Count already used slots in this range
            already_used = sum(1 for t in range(start, end + 1) if used[t])
            
            # Need to use more slots
            remaining = duration - already_used
            
            # Greedily pick latest available slots (to maximize overlap with future tasks)
            for t in range(end, start - 1, -1):
                if remaining <= 0:
                    break
                if not used[t]:
                    used[t] = True
                    remaining -= 1
        
        return sum(used)