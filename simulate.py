'''
Created on Apr 2, 2013

@author: Matt
'''
#import csv
import numpy
from matplotlib import pyplot as plt

from schedulesimulation.distribution import ExponentialDistribution
from schedulesimulation.task import Task
from schedulesimulation.fifo import Fifo

scheduler = Fifo()

# Parameters

BURST_RATE = 10
ARRIVAL_RATE = 10
N = 1000

# Setup tasks

burst_dist = ExponentialDistribution(BURST_RATE)
arrival_dist = ExponentialDistribution(ARRIVAL_RATE)

bursts = [burst_dist.getNextRate() for _ in range(N)]
bursts = [int(burst * 1000) for burst in bursts]
bursts = [1 if burst == 0 else burst for burst in bursts]

delays = [arrival_dist.getNextRate() for _ in range(N-1)]
delays = [int(delay * 1000) for delay in delays] + [0]

arrival = 0
tasks = [Task(burst=burst) for burst in bursts]
  
for task, delay in map(None, tasks, delays):
    scheduler.addtask(task)
    
    for _ in range(delay):
        scheduler.cycle()
    
scheduler.cycle_to_completion()

for task in tasks:
    print 'Task: Burst %d, Arrived %d, Ended %d, Waited %d, Turnaround %d' % (task.burst, task.start_time, task.end_time, task.wait_cycles, task.turnaround_time())
    
print 'Idle Cycles: %d' % scheduler.cycles_idle    
    