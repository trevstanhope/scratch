#!/usr/bin/python
# Tester file to use celery server
from proj.tasks import *
from celery import group
from celery import chain
from celery import chord

# Run task
event = add.delay(2,2)
state = event.state
print(state)
result = event.get(timeout=1)
print(result)
state = event.state
print(state)
event_id = event.id
print(event_id)

# Run subtask (long form) and countdown 10 seconds before executing
sub = add.subtask((2, 2), countdown=2)
event = sub.delay()
result = event.get()
print(result)

# Run subtask (short form)
sub = add.s(2,2)
event = sub.delay()
result = event.get()
print(result)

# Run partial (short form), did not get all arguments
partial = add.s(2)
event = partial.delay(8) # calls the task with delay with 2nd argument
result = event.get()

# Run a group of tasks
print(group(add.s(i, i) for i in xrange(10))().get())

# Run a group of partials
g = group(add.s(i) for i in xrange(10))
print(g(10).get())

# Run chain
print(chain(add.s(4, 4) | mul.s(8))().get())

# Run partial chain
c = chain(add.s(4) | mul.s(8))
print(c(4).get())

# Run chord
print(chord((add.s(i, i) for i in xrange(10)), xsum.s())().get())
