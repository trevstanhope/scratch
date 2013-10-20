#!/usr/bin/env python
# Bayesian with five greedy and 5 simulated annearling learners serially
# http://pythonhosted.org/pebl/tutorial.html

from pebl import data, result
from pebl.learner import greedy, simanneal
dataset = data.fromfile("pebl-tutorial-data2.txt")
learners = [ greedy.GreedyLearner(dataset, max_iterations=1000000) for i in range(5) ] + \
  [ simanneal.SimulatedAnnealingLearner(dataset) for i in range(5) ]
merged_result = result.merge([learner.run() for learner in learners])
merged_result.tofile("example3-result")
