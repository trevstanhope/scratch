#!/usr/bin/env python
# Bayesian with five greedy and 5 simulated annearling learners serially
# http://pythonhosted.org/pebl/tutorial.html

from pebl import data, result
from pebl.learner import greedy, simanneal
from pebl.taskcontroller import multiprocess
dataset = data.fromfile("pebl-tutorial-data2.txt")
learners = [ greedy.GreedyLearner(dataset, max_iterations=1000000) for i in range(5) ] + \
  [ simanneal.SimulatedAnnealingLearner(dataset) for i in range(5) ]
tc = multiprocess.MultiProcessController(poolsize=2)
results = tc.run(learners)
merged_result = result.merge(results)
merged_result.tofile("example4-result")
