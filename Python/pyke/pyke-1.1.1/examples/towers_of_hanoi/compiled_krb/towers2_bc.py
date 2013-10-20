# towers2_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def solve(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                tuple(range(context.lookup_data('n')))):
          context.end_save_all_undo()
          with engine.prove(rule.rule_base.root_name, 'solve2', context,
                            (rule.pattern(1),
                             rule.pattern(2),
                             rule.pattern(3),
                             rule.pattern(4),
                             rule.pattern(5),)) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "towers2.solve: got unexpected plan from when clause 2"
              rule.rule_base.num_bc_rule_successes += 1
              yield
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def solve2_done(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def solve2_not_done(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'move', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "towers2.solve2_not_done: got unexpected plan from when clause 1"
            if context.lookup_data('from') != context.lookup_data('last_move'):
              mark3 = context.mark(True)
              if rule.pattern(3).match_data(context, context,
                      (context.lookup_data('a'), context.lookup_data('b'), context.lookup_data('c'))):
                context.end_save_all_undo()
                if context.lookup_data('freeze') not in context.lookup_data('frozen_boards'):
                  with engine.prove(rule.rule_base.root_name, 'solve2', context,
                                    (rule.pattern(1),
                                     rule.pattern(4),
                                     rule.pattern(5),
                                     rule.pattern(6),
                                     rule.pattern(7),)) \
                    as gen_5:
                    for x_5 in gen_5:
                      assert x_5 is None, \
                        "towers2.solve2_not_done: got unexpected plan from when clause 5"
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark3)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def move(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        for python_ans in \
             range(3):
          mark1 = context.mark(True)
          if rule.pattern(0).match_data(context, context, python_ans):
            context.end_save_all_undo()
            if len(context.lookup_data('old_board')[context.lookup_data('from')]) > 0:
              for python_ans in \
                   range(3):
                mark3 = context.mark(True)
                if rule.pattern(1).match_data(context, context, python_ans):
                  context.end_save_all_undo()
                  if context.lookup_data('from') != context.lookup_data('to'):
                    mark5 = context.mark(True)
                    if rule.pattern(2).match_data(context, context,
                            context.lookup_data('old_board')[context.lookup_data('from')][0]):
                      context.end_save_all_undo()
                      mark6 = context.mark(True)
                      if rule.pattern(3).match_data(context, context,
                              context.lookup_data('old_board')[context.lookup_data('to')]):
                        context.end_save_all_undo()
                        with engine.prove(rule.rule_base.root_name, 'ok', context,
                                          (rule.pattern(2),
                                           rule.pattern(3),)) \
                          as gen_7:
                          for x_7 in gen_7:
                            assert x_7 is None, \
                              "towers2.move: got unexpected plan from when clause 7"
                            mark8 = context.mark(True)
                            if rule.pattern(4).match_data(context, context,
                                    tuple((pile[1:] if i == context.lookup_data('from')
                                   else (context.lookup_data('top'),) + pile if i == context.lookup_data('to')
                                   else pile)
                                   for i, pile in enumerate(context.lookup_data('old_board')))):
                              context.end_save_all_undo()
                              rule.rule_base.num_bc_rule_successes += 1
                              yield
                            else: context.end_save_all_undo()
                            context.undo_to_mark(mark8)
                      else: context.end_save_all_undo()
                      context.undo_to_mark(mark6)
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark5)
                else: context.end_save_all_undo()
                context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ok_empty(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ok_smaller(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        if context.lookup_data('disc') < context.lookup_data('top'):
          rule.rule_base.num_bc_rule_successes += 1
          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('towers2')
  
  bc_rule.bc_rule('solve', This_rule_base, 'solve',
                  solve, None,
                  (contexts.variable('n'),
                   contexts.variable('moves'),),
                  (),
                  (contexts.variable('disks'),
                   pattern.pattern_tuple((contexts.variable('disks'), pattern.pattern_literal(()), pattern.pattern_literal(()),), None),
                   pattern.pattern_tuple((pattern.pattern_literal(()), pattern.pattern_literal(()), contexts.variable('disks'),), None),
                   pattern.pattern_literal(1),
                   pattern.pattern_tuple((pattern.pattern_tuple((contexts.variable('disks'), pattern.pattern_literal(()), pattern.pattern_literal(()),), None),), None),
                   contexts.variable('moves'),))
  
  bc_rule.bc_rule('solve2_done', This_rule_base, 'solve2',
                  solve2_done, None,
                  (pattern.pattern_tuple((contexts.variable('a'), contexts.variable('b'), contexts.variable('c'),), None),
                   pattern.pattern_tuple((contexts.variable('a'), contexts.variable('b'), contexts.variable('c'),), None),
                   contexts.anonymous('_last_move'),
                   contexts.anonymous('_frozen_boards'),
                   pattern.pattern_literal(()),),
                  (),
                  ())
  
  bc_rule.bc_rule('solve2_not_done', This_rule_base, 'solve2',
                  solve2_not_done, None,
                  (pattern.pattern_tuple((contexts.variable('a1'), contexts.variable('b1'), contexts.variable('c1'),), None),
                   pattern.pattern_tuple((contexts.variable('a2'), contexts.variable('b2'), contexts.variable('c2'),), None),
                   contexts.variable('last_move'),
                   contexts.variable('frozen_boards'),
                   pattern.pattern_tuple((pattern.pattern_tuple((contexts.variable('from'), contexts.variable('to'),), None),), contexts.variable('moves')),),
                  (),
                  (pattern.pattern_tuple((contexts.variable('a1'), contexts.variable('b1'), contexts.variable('c1'),), None),
                   pattern.pattern_tuple((contexts.variable('a'), contexts.variable('b'), contexts.variable('c'),), None),
                   pattern.pattern_tuple((contexts.variable('from'), contexts.variable('to'),), None),
                   contexts.variable('freeze'),
                   pattern.pattern_tuple((contexts.variable('a2'), contexts.variable('b2'), contexts.variable('c2'),), None),
                   contexts.variable('to'),
                   pattern.pattern_tuple((contexts.variable('freeze'),), contexts.variable('frozen_boards')),
                   contexts.variable('moves'),))
  
  bc_rule.bc_rule('move', This_rule_base, 'move',
                  move, None,
                  (contexts.variable('old_board'),
                   contexts.variable('new_board'),
                   pattern.pattern_tuple((contexts.variable('from'), contexts.variable('to'),), None),),
                  (),
                  (contexts.variable('from'),
                   contexts.variable('to'),
                   contexts.variable('top'),
                   contexts.variable('to_pile'),
                   contexts.variable('new_board'),))
  
  bc_rule.bc_rule('ok_empty', This_rule_base, 'ok',
                  ok_empty, None,
                  (contexts.anonymous('_disc'),
                   pattern.pattern_literal(()),),
                  (),
                  ())
  
  bc_rule.bc_rule('ok_smaller', This_rule_base, 'ok',
                  ok_smaller, None,
                  (contexts.variable('disc'),
                   pattern.pattern_tuple((contexts.variable('top'),), contexts.anonymous('_rest')),),
                  (),
                  ())


Krb_filename = '../towers2.krb'
Krb_lineno_map = (
    ((16, 20), (7, 7)),
    ((24, 24), (9, 9)),
    ((26, 35), (10, 11)),
    ((50, 54), (14, 14)),
    ((68, 72), (17, 18)),
    ((74, 81), (20, 20)),
    ((82, 82), (21, 21)),
    ((85, 85), (22, 22)),
    ((87, 87), (23, 23)),
    ((88, 97), (24, 25)),
    ((112, 116), (28, 28)),
    ((119, 119), (30, 30)),
    ((123, 123), (31, 31)),
    ((125, 125), (32, 32)),
    ((129, 129), (33, 33)),
    ((132, 132), (34, 34)),
    ((136, 136), (35, 35)),
    ((138, 144), (36, 36)),
    ((147, 150), (37, 40)),
    ((174, 178), (43, 43)),
    ((192, 196), (46, 46)),
    ((198, 198), (48, 48)),
)
