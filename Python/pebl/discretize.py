from pebl import data
dataset = data.fromfile("pebl-tutorial-data1.txt")
dataset.discretize(numbins=3)
for i,s in enumerate(dataset.samples):
  s.name = "sample-%d" % i
dataset.tofile("pebl-tutorial-data2.txt")
