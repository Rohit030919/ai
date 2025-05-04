class Job:
    def __init__(self, job_id, deadline, profit):
        self.id = job_id      # Job identifier (e.g., 'J1')
        self.deadline = deadline  # Deadline by which job must be completed
        self.profit = profit  # Profit earned if job is completed by deadline

def job_scheduling(jobs):
    # Step 1: Sort all jobs in descending order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)
    
    # Step 2: Find maximum deadline to determine array size
    max_deadline = max(job.deadline for job in jobs)
    
    # Step 3: Initialize result and slot tracking arrays
    result = [None] * max_deadline  # To store scheduled jobs
    slot = [False] * max_deadline   # To track available time slots
    total_profit = 0
    job_sequence = []
    
    # Step 4: Iterate through each job in profit order
    for job in jobs:
        # Step 5: Try to schedule job in latest possible slot before deadline
        for time_slot in range(min(max_deadline, job.deadline) - 1, -1, -1):
            if not slot[time_slot]:
                slot[time_slot] = True
                result[time_slot] = job.id
                total_profit += job.profit
                job_sequence.append(job.id)
                break
    
    # Step 6: Return the sequence of jobs and total profit
    return job_sequence, total_profit

# Example usage
jobs_list = [
    Job('J1', 2, 100),
    Job('J2', 1, 19),
    Job('J3', 2, 27),
    Job('J4', 1, 25),
    Job('J5', 3, 15)
]

sequence, profit = job_scheduling(jobs_list)
print("Job Sequence:", sequence)
print("Total Profit:", profit)