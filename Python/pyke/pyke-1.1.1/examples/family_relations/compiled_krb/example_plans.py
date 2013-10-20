# example_plans.py

pyke_version = '1.1.1'
compiler_version = 1

def how_related_child_parent(context):
  return (context['plan#2'])((context['p1_type']), (context['p2_type']))

def how_related_parent_child(context):
  return (context['plan#2'])((context['p1_type']), (context['p2_type']))

def how_related_siblings(context):
  return (context['p1_type']) + ', ' + (context['p2_type'])

def how_related_nn_au(context):
  return (context['plan#2'])((context['p1_type']), (context['p2_type']))

def how_related_au_nn(context):
  return (context['plan#2'])((context['p1_type']), (context['p2_type']))

def how_related_cousins(context):
  return (context['plan#2'])()

def how_related_removed_cousins(context):
  nth_cousin = (context['plan#3'])()
  return "%s, %d removed" % (nth_cousin, (context['r1']))

def how_related_cousins_removed(context):
  nth_cousin = (context['plan#3'])()
  return "%s, %d removed" % (nth_cousin, (context['r1']))

def nth_cousin_th(context):
  return "%dth cousins" % (context['n'])

def nth_cousin_1(context):
  return "%dst cousins" % (context['n'])

def nth_cousin_2(context):
  return "%dnd cousins" % (context['n'])

def nth_cousin_3(context):
  return "%drd cousins" % (context['n'])

def add_empty_prefix(context, x, y):
  return x + ', ' + y

def add_prefix(context, x, y):
  pre = ' '.join((context['prefix'])) + ' '
  return pre + x + ', ' + pre + y


Krb_filename = '../example.krb'
