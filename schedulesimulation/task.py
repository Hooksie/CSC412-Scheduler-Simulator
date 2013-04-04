'''
Created on Apr 2, 2013

@author: Matt
'''
    
class Task(object):
    
    def __init__(self, burst=0):
        self.burst = burst
        self._burst_remaining = burst
        
        self.wait_cycles = 0
        self.start_time = 0
        self.end_time = 0
        
    @property
    def burst_remaining(self):
        return self._burst_remaining
    
    @burst_remaining.setter
    def burst_remaining(self, value):
        if value >= 0:
            self._burst_remaining = value
        else:
            raise ValueError('burst_remaining cannot be negative')
        
    def turnaround_time(self):
        
        if self.end_time >= self.start_time:
            return self.end_time - self.start_time
        else:
            raise ValueError('Start and end times cannot be')
        
    def wait_a_cycle(self):
        self.wait_cycles += 1
        
    def finished(self):
        return self.burst_remaining == 0