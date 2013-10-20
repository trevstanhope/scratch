# towers_of_hanoi_bc.py

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
                            (rule.pattern(0),
                             rule.pattern(1),
                             rule.pattern(1),
                             rule.pattern(1),
                             rule.pattern(1),
                             rule.pattern(0),
                             rule.pattern(2),
                             rule.pattern(3),
                             rule.pattern(4),)) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "towers_of_hanoi.solve: got unexpected plan from when clause 2"
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
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),
                           rule.pattern(5),
                           rule.pattern(6),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "towers_of_hanoi.solve2_not_done: got unexpected plan from when clause 1"
            if context.lookup_data('from') != context.lookup_data('last_move'):
              mark3 = context.mark(True)
              if rule.pattern(7).match_data(context, context,
                      (context.lookup_data('a'), context.lookup_data('b'), context.lookup_data('c'))):
                context.end_save_all_undo()
                if context.lookup_data('freeze') not in context.lookup_data('frozen_boards'):
                  with engine.prove(rule.rule_base.root_name, 'solve2', context,
                                    (rule.pattern(3),
                                     rule.pattern(4),
                                     rule.pattern(5),
                                     rule.pattern(8),
                                     rule.pattern(9),
                                     rule.pattern(10),
                                     rule.pattern(11),
                                     rule.pattern(12),
                                     rule.pattern(13),)) \
                    as gen_5:
                    for x_5 in gen_5:
                      assert x_5 is None, \
                        "towers_of_hanoi.solve2_not_done: got unexpected plan from when clause 5"
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark3)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def move_01(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'ok', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "towers_of_hanoi.move_01: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def move_02(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'ok', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "towers_of_hanoi.move_02: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def move_10(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'ok', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "towers_of_hanoi.move_10: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def move_12(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'ok', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "towers_of_hanoi.move_12: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def move_20(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'ok', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "towers_of_hanoi.move_20: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def move_21(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'ok', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "towers_of_hanoi.move_21: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
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
  This_rule_base = engine.get_create('towers_of_hanoi')
  
  bc_rule.bc_rule('solve', This_rule_base, 'solve',
                  solve, None,
                  (contexts.variable('n'),
                   contexts.variable('moves'),),
                  (),
                  (contexts.variable('disks'),
                   pattern.pattern_literal(()),
                   pattern.pattern_literal(1),
                   pattern.pattern_tuple((pattern.pattern_tuple((contexts.variable('disks'), pattern.pattern_literal(()), pattern.pattern_literal(()),), None),), None),
                   contexts.variable('moves'),))
  
  bc_rule.bc_rule('solve2_done', This_rule_base, 'solve2',
                  solve2_done, None,
                  (contexts.variable('a'),
                   contexts.variable('b'),
                   contexts.variable('c'),
                   contexts.variable('a'),
                   contexts.variable('b'),
                   contexts.variable('c'),
                   contexts.anonymous('_last_move'),
                   contexts.anonymous('_frozen_boards'),
                   pattern.pattern_literal(()),),
                  (),
                  ())
  
  bc_rule.bc_rule('solve2_not_done', This_rule_base, 'solve2',
                  solve2_not_done, None,
                  (contexts.variable('a1'),
                   contexts.variable('b1'),
                   contexts.variable('c1'),
                   contexts.variable('a2'),
                   contexts.variable('b2'),
                   contexts.variable('c2'),
                   contexts.variable('last_move'),
                   contexts.variable('frozen_boards'),
                   pattern.pattern_tuple((pattern.pattern_tuple((contexts.variable('from'), contexts.variable('to'),), None),), contexts.variable('moves')),),
                  (),
                  (contexts.variable('a1'),
                   contexts.variable('b1'),
                   contexts.variable('c1'),
                   contexts.variable('a'),
                   contexts.variable('b'),
                   contexts.variable('c'),
                   pattern.pattern_tuple((contexts.variable('from'), contexts.variable('to'),), None),
                   contexts.variable('freeze'),
                   contexts.variable('a2'),
                   contexts.variable('b2'),
                   contexts.variable('c2'),
                   contexts.variable('to'),
                   pattern.pattern_tuple((contexts.variable('freeze'),), contexts.variable('frozen_boards')),
                   contexts.variable('moves'),))
  
  bc_rule.bc_rule('move_01', This_rule_base, 'move',
                  move_01, None,
                  (pattern.pattern_tuple((contexts.variable('a1'),), contexts.variable('as')),
                   contexts.variable('b'),
                   contexts.variable('c'),
                   contexts.variable('as'),
                   pattern.pattern_tuple((contexts.variable('a1'),), contexts.variable('b')),
                   contexts.variable('c'),
                   pattern.pattern_literal((0, 1,)),),
                  (),
                  (contexts.variable('a1'),
                   contexts.variable('b'),))
  
  bc_rule.bc_rule('move_02', This_rule_base, 'move',
                  move_02, None,
                  (pattern.pattern_tuple((contexts.variable('a1'),), contexts.variable('as')),
                   contexts.variable('b'),
                   contexts.variable('c'),
                   contexts.variable('as'),
                   contexts.variable('b'),
                   pattern.pattern_tuple((contexts.variable('a1'),), contexts.variable('c')),
                   pattern.pattern_literal((0, 2,)),),
                  (),
                  (contexts.variable('a1'),
                   contexts.variable('c'),))
  
  bc_rule.bc_rule('move_10', This_rule_base, 'move',
                  move_10, None,
                  (contexts.variable('a'),
                   pattern.pattern_tuple((contexts.variable('b1'),), contexts.variable('bs')),
                   contexts.variable('c'),
                   pattern.pattern_tuple((contexts.variable('b1'),), contexts.variable('a')),
                   contexts.variable('bs'),
                   contexts.variable('c'),
                   pattern.pattern_literal((1, 0,)),),
                  (),
                  (contexts.variable('b1'),
                   contexts.variable('a'),))
  
  bc_rule.bc_rule('move_12', This_rule_base, 'move',
                  move_12, None,
                  (contexts.variable('a'),
                   pattern.pattern_tuple((contexts.variable('b1'),), contexts.variable('bs')),
                   contexts.variable('c'),
                   contexts.variable('a'),
                   contexts.variable('bs'),
                   pattern.pattern_tuple((contexts.variable('b1'),), contexts.variable('c')),
                   pattern.pattern_literal((1, 2,)),),
                  (),
                  (contexts.variable('b1'),
                   contexts.variable('c'),))
  
  bc_rule.bc_rule('move_20', This_rule_base, 'move',
                  move_20, None,
                  (contexts.variable('a'),
                   contexts.variable('b'),
                   pattern.pattern_tuple((contexts.variable('c1'),), contexts.variable('cs')),
                   pattern.pattern_tuple((contexts.variable('c1'),), contexts.variable('a')),
                   contexts.variable('b'),
                   contexts.variable('cs'),
                   pattern.pattern_literal((2, 0,)),),
                  (),
                  (contexts.variable('c1'),
                   contexts.variable('a'),))
  
  bc_rule.bc_rule('move_21', This_rule_base, 'move',
                  move_21, None,
                  (contexts.variable('a'),
                   contexts.variable('b'),
                   pattern.pattern_tuple((contexts.variable('c1'),), contexts.variable('cs')),
                   contexts.variable('a'),
                   pattern.pattern_tuple((contexts.variable('c1'),), contexts.variable('b')),
                   contexts.variable('cs'),
                   pattern.pattern_literal((2, 1,)),),
                  (),
                  (contexts.variable('c1'),
                   contexts.variable('b'),))
  
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


Krb_filename = '../towers_of_hanoi.krb'
Krb_lineno_map = (
    ((16, 20), (16, 16)),
    ((24, 24), (18, 18)),
    ((26, 39), (19, 19)),
    ((54, 58), (22, 22)),
    ((72, 76), (25, 26)),
    ((78, 89), (28, 28)),
    ((90, 90), (29, 29)),
    ((93, 93), (30, 30)),
    ((95, 95), (31, 31)),
    ((96, 109), (32, 33)),
    ((124, 128), (36, 36)),
    ((130, 136), (38, 38)),
    ((149, 153), (41, 41)),
    ((155, 161), (43, 43)),
    ((174, 178), (46, 46)),
    ((180, 186), (48, 48)),
    ((199, 203), (51, 51)),
    ((205, 211), (53, 53)),
    ((224, 228), (56, 56)),
    ((230, 236), (58, 58)),
    ((249, 253), (61, 61)),
    ((255, 261), (63, 63)),
    ((274, 278), (66, 66)),
    ((292, 296), (69, 69)),
    ((298, 298), (71, 71)),
)
