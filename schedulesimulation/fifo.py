from collections import deque

class Fifo(object):
    
    def __init__(self):
        self.cycles = 0
        self.cycles_idle = 0
        self.current_task = None
        self.taskqueue = deque()

    def cycle(self):
        self.cycles += 1
        
        if self.current_task is not None:
            self.cycle_current_task()
        
        elif self.taskqueue:
            self.current_task = self.taskqueue.popleft()
            self.cycle_current_task()
            
        else:
            self.cycles_idle += 1
    
    def cycle_to_completion(self):
        while (self.current_task is not None) or self.taskqueue:
            self.cycle()
            
    def cycle_current_task(self):
        self.current_task.burst_remaining -= 1
        
        for queued in self.taskqueue:
            queued.wait_a_cycle()
                
        if self.current_task.finished():
            self.current_task.end_time = self.cycles
            self.current_task = None
 
    def addtask(self, task):
        task.start_time = self.cycles
        self.taskqueue.append(task)