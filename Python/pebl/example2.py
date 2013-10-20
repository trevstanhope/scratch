#!/usr/bin/env python
# http://pythonhosted.org/pebl/tutorial.html

from pebl import data, result
from pebl.learner import greedy
dataset = data.fromfile("pebl-tutorial-data2.txt")
learner1 = greedy.GreedyLearner(dataset, max_iterations=1000000)
learner2 = greedy.GreedyLearner(dataset, max_time=120) # in seconds
result1 = learner1.run()
result2 = learner2.run()
merged_result = result.merge(result1, result2)
merged_result.tofile("example2-result")
