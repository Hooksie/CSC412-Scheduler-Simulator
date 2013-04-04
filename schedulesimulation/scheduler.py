from collections import deque

class Scheduler():
    
    def __init__(self):
        self.cycles = 0
        self.cycles_idle = 0
        self.current_task = None
        self.taskqueue = deque()
