# bc2_example_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def father_son(rule, arg_patterns, arg_context):
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
        with engine.prove('family', 'son_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.father_son: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def mother_son(rule, arg_patterns, arg_context):
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
        with engine.prove('family', 'son_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.mother_son: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def father_daughter(rule, arg_patterns, arg_context):
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
        with engine.prove('family', 'daughter_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.father_daughter: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def mother_daughter(rule, arg_patterns, arg_context):
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
        with engine.prove('family', 'daughter_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.mother_daughter: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def brothers(rule, arg_patterns, arg_context):
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
        with engine.prove('family', 'son_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.brothers: got unexpected plan from when clause 1"
            with engine.prove('family', 'son_of', context,
                              (rule.pattern(3),
                               rule.pattern(1),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc2_example.brothers: got unexpected plan from when clause 2"
                if context.lookup_data('brother1') != context.lookup_data('brother2'):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sisters(rule, arg_patterns, arg_context):
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
        with engine.prove('family', 'daughter_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.sisters: got unexpected plan from when clause 1"
            with engine.prove('family', 'daughter_of', context,
                              (rule.pattern(3),
                               rule.pattern(1),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc2_example.sisters: got unexpected plan from when clause 2"
                if context.lookup_data('sister1') != context.lookup_data('sister2'):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def brother_sister(rule, arg_patterns, arg_context):
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
        with engine.prove('family', 'daughter_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.brother_sister: got unexpected plan from when clause 1"
            with engine.prove('family', 'son_of', context,
                              (rule.pattern(3),
                               rule.pattern(1),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc2_example.brother_sister: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sister_brother(rule, arg_patterns, arg_context):
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
        with engine.prove('family', 'son_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.sister_brother: got unexpected plan from when clause 1"
            with engine.prove('family', 'daughter_of', context,
                              (rule.pattern(3),
                               rule.pattern(1),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc2_example.sister_brother: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def as_au_brother_uncle(rule, arg_patterns, arg_context):
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

def as_au_sister_aunt(rule, arg_patterns, arg_context):
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

def as_nn_son_nephew(rule, arg_patterns, arg_context):
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

def as_nn_daughter_niece(rule, arg_patterns, arg_context):
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

def niece_or_nephew_and_aunt_or_uncle_1(rule, arg_patterns, arg_context):
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
        if context.is_bound(contexts.variable('nn')):
          with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                            (rule.pattern(0),
                             rule.pattern(1),
                             rule.pattern(2),
                             rule.pattern(3),
                             rule.pattern(4),)) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "bc2_example.niece_or_nephew_and_aunt_or_uncle_1: got unexpected plan from when clause 2"
              with engine.prove(rule.rule_base.root_name, 'siblings', context,
                                (rule.pattern(1),
                                 rule.pattern(5),
                                 rule.pattern(6),
                                 rule.pattern(3),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc2_example.niece_or_nephew_and_aunt_or_uncle_1: got unexpected plan from when clause 3"
                  with engine.prove(rule.rule_base.root_name, 'as_au', context,
                                    (rule.pattern(6),
                                     rule.pattern(7),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "bc2_example.niece_or_nephew_and_aunt_or_uncle_1: got unexpected plan from when clause 4"
                      with engine.prove(rule.rule_base.root_name, 'as_nn', context,
                                        (rule.pattern(4),
                                         rule.pattern(8),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "bc2_example.niece_or_nephew_and_aunt_or_uncle_1: got unexpected plan from when clause 5"
                          mark6 = context.mark(True)
                          if rule.pattern(9).match_data(context, context,
                                  ('great',) * len(context.lookup_data('depth'))):
                            context.end_save_all_undo()
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
                          else: context.end_save_all_undo()
                          context.undo_to_mark(mark6)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def niece_or_nephew_and_aunt_or_uncle_2(rule, arg_patterns, arg_context):
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
        if not context.is_bound(contexts.variable('nn')):
          with engine.prove(rule.rule_base.root_name, 'siblings', context,
                            (rule.pattern(0),
                             rule.pattern(1),
                             rule.pattern(2),
                             rule.pattern(3),)) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "bc2_example.niece_or_nephew_and_aunt_or_uncle_2: got unexpected plan from when clause 2"
              with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                                (rule.pattern(4),
                                 rule.pattern(1),
                                 rule.pattern(5),
                                 rule.pattern(2),
                                 rule.pattern(6),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc2_example.niece_or_nephew_and_aunt_or_uncle_2: got unexpected plan from when clause 3"
                  with engine.prove(rule.rule_base.root_name, 'as_au', context,
                                    (rule.pattern(3),
                                     rule.pattern(7),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "bc2_example.niece_or_nephew_and_aunt_or_uncle_2: got unexpected plan from when clause 4"
                      with engine.prove(rule.rule_base.root_name, 'as_nn', context,
                                        (rule.pattern(6),
                                         rule.pattern(8),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "bc2_example.niece_or_nephew_and_aunt_or_uncle_2: got unexpected plan from when clause 5"
                          mark6 = context.mark(True)
                          if rule.pattern(9).match_data(context, context,
                                  ('great',) * len(context.lookup_data('depth'))):
                            context.end_save_all_undo()
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
                          else: context.end_save_all_undo()
                          context.undo_to_mark(mark6)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def parent_and_child(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.parent_and_child: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def grand_parent_and_child_1(rule, arg_patterns, arg_context):
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
        if context.is_bound(contexts.variable('child')):
          with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                            (rule.pattern(0),
                             rule.pattern(1),
                             rule.pattern(2),
                             rule.pattern(3),)) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "bc2_example.grand_parent_and_child_1: got unexpected plan from when clause 2"
              with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                                (rule.pattern(1),
                                 rule.pattern(4),
                                 rule.pattern(5),
                                 rule.pattern(2),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc2_example.grand_parent_and_child_1: got unexpected plan from when clause 3"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def grand_parent_and_child_2(rule, arg_patterns, arg_context):
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
        if not context.is_bound(contexts.variable('child')):
          with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                            (rule.pattern(0),
                             rule.pattern(1),
                             rule.pattern(2),
                             rule.pattern(3),)) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "bc2_example.grand_parent_and_child_2: got unexpected plan from when clause 2"
              with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                                (rule.pattern(4),
                                 rule.pattern(0),
                                 rule.pattern(3),
                                 rule.pattern(5),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc2_example.grand_parent_and_child_2: got unexpected plan from when clause 3"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def great_grand_parent_and_child_1(rule, arg_patterns, arg_context):
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
        if context.is_bound(contexts.variable('child')):
          with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                            (rule.pattern(0),
                             rule.pattern(1),
                             rule.pattern(2),
                             rule.pattern(3),)) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "bc2_example.great_grand_parent_and_child_1: got unexpected plan from when clause 2"
              with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                                (rule.pattern(1),
                                 rule.pattern(4),
                                 rule.pattern(5),
                                 rule.pattern(6),
                                 rule.pattern(2),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc2_example.great_grand_parent_and_child_1: got unexpected plan from when clause 3"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def great_grand_parent_and_child_2(rule, arg_patterns, arg_context):
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
        if not context.is_bound(contexts.variable('child')):
          with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                            (rule.pattern(0),
                             rule.pattern(1),
                             rule.pattern(2),
                             rule.pattern(3),)) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "bc2_example.great_grand_parent_and_child_2: got unexpected plan from when clause 2"
              with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                                (rule.pattern(4),
                                 rule.pattern(0),
                                 rule.pattern(5),
                                 rule.pattern(3),
                                 rule.pattern(6),)) \
                as gen_3:
                for x_3 in gen_3:
                  assert x_3 is None, \
                    "bc2_example.great_grand_parent_and_child_2: got unexpected plan from when clause 3"
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def first_cousins(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.first_cousins: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'siblings', context,
                              (rule.pattern(1),
                               rule.pattern(3),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc2_example.first_cousins: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                                  (rule.pattern(4),
                                   rule.pattern(3),
                                   rule.pattern(2),
                                   rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc2_example.first_cousins: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def nth_cousins(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.nth_cousins: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'cousins', context,
                              (rule.pattern(1),
                               rule.pattern(3),
                               rule.pattern(4),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc2_example.nth_cousins: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                                  (rule.pattern(5),
                                   rule.pattern(3),
                                   rule.pattern(2),
                                   rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc2_example.nth_cousins: got unexpected plan from when clause 3"
                    mark4 = context.mark(True)
                    if rule.pattern(6).match_data(context, context,
                            context.lookup_data('n') + 1):
                      context.end_save_all_undo()
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark4)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def how_related_child_parent(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.how_related_child_parent: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(5).match_data(context, context,
                    add_prefix(context.lookup_data('prefix'), context.lookup_data('p1_type'), context.lookup_data('p2_type'))):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def how_related_parent_child(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.how_related_parent_child: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(5).match_data(context, context,
                    add_prefix(context.lookup_data('prefix'), context.lookup_data('p1_type'), context.lookup_data('p2_type'))):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def how_related_siblings(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'siblings', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.how_related_siblings: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def how_related_nn_au(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'nn_au', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.how_related_nn_au: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(5).match_data(context, context,
                    add_prefix(context.lookup_data('prefix'), context.lookup_data('p1_type'), context.lookup_data('p2_type'))):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def how_related_au_nn(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'nn_au', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.how_related_au_nn: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(5).match_data(context, context,
                    add_prefix(context.lookup_data('prefix'), context.lookup_data('p1_type'), context.lookup_data('p2_type'))):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def how_related_cousins(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'cousins', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.how_related_cousins: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(3).match_data(context, context,
                    nth(context.lookup_data('n'))):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def how_related_removed_cousins(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(3),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.how_related_removed_cousins: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'cousins', context,
                              (rule.pattern(1),
                               rule.pattern(4),
                               rule.pattern(5),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc2_example.how_related_removed_cousins: got unexpected plan from when clause 2"
                mark3 = context.mark(True)
                if rule.pattern(6).match_data(context, context,
                        nth(context.lookup_data('n'))):
                  context.end_save_all_undo()
                  mark4 = context.mark(True)
                  if rule.pattern(7).match_data(context, context,
                          len(context.lookup_data('grand')) + 1):
                    context.end_save_all_undo()
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark4)
                else: context.end_save_all_undo()
                context.undo_to_mark(mark3)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def how_related_cousins_removed(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'cousins', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.how_related_cousins_removed: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                              (rule.pattern(3),
                               rule.pattern(1),
                               rule.pattern(4),
                               rule.pattern(5),
                               rule.pattern(5),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc2_example.how_related_cousins_removed: got unexpected plan from when clause 2"
                mark3 = context.mark(True)
                if rule.pattern(6).match_data(context, context,
                        nth(context.lookup_data('n'))):
                  context.end_save_all_undo()
                  mark4 = context.mark(True)
                  if rule.pattern(7).match_data(context, context,
                          len(context.lookup_data('grand')) + 1):
                    context.end_save_all_undo()
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark4)
                else: context.end_save_all_undo()
                context.undo_to_mark(mark3)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc2_example')
  
  bc_rule.bc_rule('father_son', This_rule_base, 'child_parent',
                  father_son, None,
                  (contexts.variable('child'),
                   contexts.variable('father'),
                   pattern.pattern_literal('father'),
                   pattern.pattern_literal('son'),),
                  (),
                  (contexts.variable('child'),
                   contexts.variable('father'),
                   contexts.variable('mother'),))
  
  bc_rule.bc_rule('mother_son', This_rule_base, 'child_parent',
                  mother_son, None,
                  (contexts.variable('child'),
                   contexts.variable('mother'),
                   pattern.pattern_literal('mother'),
                   pattern.pattern_literal('son'),),
                  (),
                  (contexts.variable('child'),
                   contexts.variable('father'),
                   contexts.variable('mother'),))
  
  bc_rule.bc_rule('father_daughter', This_rule_base, 'child_parent',
                  father_daughter, None,
                  (contexts.variable('child'),
                   contexts.variable('father'),
                   pattern.pattern_literal('father'),
                   pattern.pattern_literal('daughter'),),
                  (),
                  (contexts.variable('child'),
                   contexts.variable('father'),
                   contexts.variable('mother'),))
  
  bc_rule.bc_rule('mother_daughter', This_rule_base, 'child_parent',
                  mother_daughter, None,
                  (contexts.variable('child'),
                   contexts.variable('mother'),
                   pattern.pattern_literal('mother'),
                   pattern.pattern_literal('daughter'),),
                  (),
                  (contexts.variable('child'),
                   contexts.variable('father'),
                   contexts.variable('mother'),))
  
  bc_rule.bc_rule('brothers', This_rule_base, 'siblings',
                  brothers, None,
                  (contexts.variable('brother1'),
                   contexts.variable('brother2'),
                   pattern.pattern_literal('brother'),
                   pattern.pattern_literal('brother'),),
                  (),
                  (contexts.variable('brother1'),
                   contexts.variable('father'),
                   contexts.variable('mother'),
                   contexts.variable('brother2'),))
  
  bc_rule.bc_rule('sisters', This_rule_base, 'siblings',
                  sisters, None,
                  (contexts.variable('sister1'),
                   contexts.variable('sister2'),
                   pattern.pattern_literal('sister'),
                   pattern.pattern_literal('sister'),),
                  (),
                  (contexts.variable('sister1'),
                   contexts.variable('father'),
                   contexts.variable('mother'),
                   contexts.variable('sister2'),))
  
  bc_rule.bc_rule('brother_sister', This_rule_base, 'siblings',
                  brother_sister, None,
                  (contexts.variable('sister'),
                   contexts.variable('brother'),
                   pattern.pattern_literal('brother'),
                   pattern.pattern_literal('sister'),),
                  (),
                  (contexts.variable('sister'),
                   contexts.variable('father'),
                   contexts.variable('mother'),
                   contexts.variable('brother'),))
  
  bc_rule.bc_rule('sister_brother', This_rule_base, 'siblings',
                  sister_brother, None,
                  (contexts.variable('brother'),
                   contexts.variable('sister'),
                   pattern.pattern_literal('sister'),
                   pattern.pattern_literal('brother'),),
                  (),
                  (contexts.variable('brother'),
                   contexts.variable('father'),
                   contexts.variable('mother'),
                   contexts.variable('sister'),))
  
  bc_rule.bc_rule('as_au_brother_uncle', This_rule_base, 'as_au',
                  as_au_brother_uncle, None,
                  (pattern.pattern_literal('brother'),
                   pattern.pattern_literal('uncle'),),
                  (),
                  ())
  
  bc_rule.bc_rule('as_au_sister_aunt', This_rule_base, 'as_au',
                  as_au_sister_aunt, None,
                  (pattern.pattern_literal('sister'),
                   pattern.pattern_literal('aunt'),),
                  (),
                  ())
  
  bc_rule.bc_rule('as_nn_son_nephew', This_rule_base, 'as_nn',
                  as_nn_son_nephew, None,
                  (pattern.pattern_literal('son'),
                   pattern.pattern_literal('nephew'),),
                  (),
                  ())
  
  bc_rule.bc_rule('as_nn_daughter_niece', This_rule_base, 'as_nn',
                  as_nn_daughter_niece, None,
                  (pattern.pattern_literal('daughter'),
                   pattern.pattern_literal('niece'),),
                  (),
                  ())
  
  bc_rule.bc_rule('niece_or_nephew_and_aunt_or_uncle_1', This_rule_base, 'nn_au',
                  niece_or_nephew_and_aunt_or_uncle_1, None,
                  (contexts.variable('nn'),
                   contexts.variable('au'),
                   contexts.variable('greats'),
                   contexts.variable('au_type'),
                   contexts.variable('nn_type'),),
                  (),
                  (contexts.variable('nn'),
                   contexts.variable('parent'),
                   contexts.variable('depth'),
                   contexts.anonymous('_'),
                   contexts.variable('child_type'),
                   contexts.variable('au'),
                   contexts.variable('sibling_type'),
                   contexts.variable('au_type'),
                   contexts.variable('nn_type'),
                   contexts.variable('greats'),))
  
  bc_rule.bc_rule('niece_or_nephew_and_aunt_or_uncle_2', This_rule_base, 'nn_au',
                  niece_or_nephew_and_aunt_or_uncle_2, None,
                  (contexts.variable('nn'),
                   contexts.variable('au'),
                   contexts.variable('greats'),
                   contexts.variable('au_type'),
                   contexts.variable('nn_type'),),
                  (),
                  (contexts.variable('au'),
                   contexts.variable('parent'),
                   contexts.anonymous('_'),
                   contexts.variable('sibling_type'),
                   contexts.variable('nn'),
                   contexts.variable('depth'),
                   contexts.variable('child_type'),
                   contexts.variable('au_type'),
                   contexts.variable('nn_type'),
                   contexts.variable('greats'),))
  
  bc_rule.bc_rule('parent_and_child', This_rule_base, 'child_parent',
                  parent_and_child, None,
                  (contexts.variable('child'),
                   contexts.variable('parent'),
                   pattern.pattern_literal(()),
                   contexts.variable('parent_type'),
                   contexts.variable('child_type'),),
                  (),
                  (contexts.variable('child'),
                   contexts.variable('parent'),
                   contexts.variable('parent_type'),
                   contexts.variable('child_type'),))
  
  bc_rule.bc_rule('grand_parent_and_child_1', This_rule_base, 'child_parent',
                  grand_parent_and_child_1, None,
                  (contexts.variable('child'),
                   contexts.variable('grand_parent'),
                   pattern.pattern_literal(('grand',)),
                   contexts.variable('parent_type'),
                   contexts.variable('child_type'),),
                  (),
                  (contexts.variable('child'),
                   contexts.variable('parent'),
                   contexts.anonymous('_'),
                   contexts.variable('child_type'),
                   contexts.variable('grand_parent'),
                   contexts.variable('parent_type'),))
  
  bc_rule.bc_rule('grand_parent_and_child_2', This_rule_base, 'child_parent',
                  grand_parent_and_child_2, None,
                  (contexts.variable('child'),
                   contexts.variable('grand_parent'),
                   pattern.pattern_literal(('grand',)),
                   contexts.variable('parent_type'),
                   contexts.variable('child_type'),),
                  (),
                  (contexts.variable('parent'),
                   contexts.variable('grand_parent'),
                   contexts.variable('parent_type'),
                   contexts.anonymous('_'),
                   contexts.variable('child'),
                   contexts.variable('child_type'),))
  
  bc_rule.bc_rule('great_grand_parent_and_child_1', This_rule_base, 'child_parent',
                  great_grand_parent_and_child_1, None,
                  (contexts.variable('child'),
                   contexts.variable('grand_parent'),
                   pattern.pattern_tuple((pattern.pattern_literal('great'), contexts.variable('a'),), contexts.variable('b')),
                   contexts.variable('parent_type'),
                   contexts.variable('child_type'),),
                  (),
                  (contexts.variable('child'),
                   contexts.variable('grand_child'),
                   contexts.anonymous('_'),
                   contexts.variable('child_type'),
                   contexts.variable('grand_parent'),
                   pattern.pattern_tuple((contexts.variable('a'),), contexts.variable('b')),
                   contexts.variable('parent_type'),))
  
  bc_rule.bc_rule('great_grand_parent_and_child_2', This_rule_base, 'child_parent',
                  great_grand_parent_and_child_2, None,
                  (contexts.variable('child'),
                   contexts.variable('grand_parent'),
                   pattern.pattern_tuple((pattern.pattern_literal('great'), contexts.variable('a'),), contexts.variable('b')),
                   contexts.variable('parent_type'),
                   contexts.variable('child_type'),),
                  (),
                  (contexts.variable('parent'),
                   contexts.variable('grand_parent'),
                   contexts.variable('parent_type'),
                   contexts.anonymous('_'),
                   contexts.variable('child'),
                   pattern.pattern_tuple((contexts.variable('a'),), contexts.variable('b')),
                   contexts.variable('child_type'),))
  
  bc_rule.bc_rule('first_cousins', This_rule_base, 'cousins',
                  first_cousins, None,
                  (contexts.variable('cousin1'),
                   contexts.variable('cousin2'),
                   pattern.pattern_literal(1),),
                  (),
                  (contexts.variable('cousin1'),
                   contexts.variable('sibling1'),
                   contexts.anonymous('_'),
                   contexts.variable('sibling2'),
                   contexts.variable('cousin2'),))
  
  bc_rule.bc_rule('nth_cousins', This_rule_base, 'cousins',
                  nth_cousins, None,
                  (contexts.variable('next_cousin1'),
                   contexts.variable('next_cousin2'),
                   contexts.variable('next_n'),),
                  (),
                  (contexts.variable('next_cousin1'),
                   contexts.variable('cousin1'),
                   contexts.anonymous('_'),
                   contexts.variable('cousin2'),
                   contexts.variable('n'),
                   contexts.variable('next_cousin2'),
                   contexts.variable('next_n'),))
  
  bc_rule.bc_rule('how_related_child_parent', This_rule_base, 'how_related',
                  how_related_child_parent, None,
                  (contexts.variable('person1'),
                   contexts.variable('person2'),
                   contexts.variable('relationship'),),
                  (),
                  (contexts.variable('person1'),
                   contexts.variable('person2'),
                   contexts.variable('prefix'),
                   contexts.variable('p2_type'),
                   contexts.variable('p1_type'),
                   contexts.variable('relationship'),))
  
  bc_rule.bc_rule('how_related_parent_child', This_rule_base, 'how_related',
                  how_related_parent_child, None,
                  (contexts.variable('person1'),
                   contexts.variable('person2'),
                   contexts.variable('relationship'),),
                  (),
                  (contexts.variable('person2'),
                   contexts.variable('person1'),
                   contexts.variable('prefix'),
                   contexts.variable('p1_type'),
                   contexts.variable('p2_type'),
                   contexts.variable('relationship'),))
  
  bc_rule.bc_rule('how_related_siblings', This_rule_base, 'how_related',
                  how_related_siblings, None,
                  (contexts.variable('person1'),
                   contexts.variable('person2'),
                   pattern.pattern_tuple((contexts.variable('p1_type'), contexts.variable('p2_type'),), None),),
                  (),
                  (contexts.variable('person1'),
                   contexts.variable('person2'),
                   contexts.variable('p2_type'),
                   contexts.variable('p1_type'),))
  
  bc_rule.bc_rule('how_related_nn_au', This_rule_base, 'how_related',
                  how_related_nn_au, None,
                  (contexts.variable('person1'),
                   contexts.variable('person2'),
                   contexts.variable('relationship'),),
                  (),
                  (contexts.variable('person1'),
                   contexts.variable('person2'),
                   contexts.variable('prefix'),
                   contexts.variable('p2_type'),
                   contexts.variable('p1_type'),
                   contexts.variable('relationship'),))
  
  bc_rule.bc_rule('how_related_au_nn', This_rule_base, 'how_related',
                  how_related_au_nn, None,
                  (contexts.variable('person1'),
                   contexts.variable('person2'),
                   contexts.variable('relationship'),),
                  (),
                  (contexts.variable('person2'),
                   contexts.variable('person1'),
                   contexts.variable('prefix'),
                   contexts.variable('p1_type'),
                   contexts.variable('p2_type'),
                   contexts.variable('relationship'),))
  
  bc_rule.bc_rule('how_related_cousins', This_rule_base, 'how_related',
                  how_related_cousins, None,
                  (contexts.variable('cousin1'),
                   contexts.variable('cousin2'),
                   pattern.pattern_tuple((contexts.variable('nth'), pattern.pattern_literal('cousins'),), None),),
                  (),
                  (contexts.variable('cousin1'),
                   contexts.variable('cousin2'),
                   contexts.variable('n'),
                   contexts.variable('nth'),))
  
  bc_rule.bc_rule('how_related_removed_cousins', This_rule_base, 'how_related',
                  how_related_removed_cousins, None,
                  (contexts.variable('removed_cousin1'),
                   contexts.variable('cousin2'),
                   pattern.pattern_tuple((contexts.variable('nth'), pattern.pattern_literal('cousins'), contexts.variable('r1'), pattern.pattern_literal('removed'),), None),),
                  (),
                  (contexts.variable('removed_cousin1'),
                   contexts.variable('cousin1'),
                   contexts.variable('grand'),
                   contexts.anonymous('_'),
                   contexts.variable('cousin2'),
                   contexts.variable('n'),
                   contexts.variable('nth'),
                   contexts.variable('r1'),))
  
  bc_rule.bc_rule('how_related_cousins_removed', This_rule_base, 'how_related',
                  how_related_cousins_removed, None,
                  (contexts.variable('cousin1'),
                   contexts.variable('removed_cousin2'),
                   pattern.pattern_tuple((contexts.variable('nth'), pattern.pattern_literal('cousins'), contexts.variable('r1'), pattern.pattern_literal('removed'),), None),),
                  (),
                  (contexts.variable('cousin1'),
                   contexts.variable('cousin2'),
                   contexts.variable('n'),
                   contexts.variable('removed_cousin2'),
                   contexts.variable('grand'),
                   contexts.anonymous('_'),
                   contexts.variable('nth'),
                   contexts.variable('r1'),))

def nth(n):
    if n % 10 not in (1, 2, 3) or 10 < n % 100 < 20: return "%dth" % n
    if n % 10 == 1: return "%dst" % n
    if n % 10 == 2: return "%dnd" % n
    if n % 10 == 3: return "%drd" % n
def add_prefix(prefix, x, y):
    if not prefix: return (x, y)
    return (prefix + (x,), prefix + (y,))

Krb_filename = '../bc2_example.krb'
Krb_lineno_map = (
    ((16, 20), (25, 25)),
    ((22, 29), (27, 27)),
    ((42, 46), (30, 30)),
    ((48, 55), (32, 32)),
    ((68, 72), (35, 35)),
    ((74, 81), (37, 37)),
    ((94, 98), (40, 40)),
    ((100, 107), (42, 42)),
    ((120, 124), (46, 46)),
    ((126, 133), (48, 48)),
    ((134, 141), (49, 49)),
    ((142, 142), (50, 50)),
    ((155, 159), (53, 53)),
    ((161, 168), (55, 55)),
    ((169, 176), (56, 56)),
    ((177, 177), (57, 57)),
    ((190, 194), (60, 60)),
    ((196, 203), (62, 62)),
    ((204, 211), (63, 63)),
    ((224, 228), (66, 66)),
    ((230, 237), (68, 68)),
    ((238, 245), (69, 69)),
    ((258, 262), (72, 72)),
    ((276, 280), (75, 75)),
    ((294, 298), (78, 78)),
    ((312, 316), (81, 81)),
    ((330, 334), (84, 84)),
    ((336, 336), (86, 86)),
    ((337, 346), (87, 87)),
    ((347, 355), (88, 88)),
    ((356, 362), (89, 89)),
    ((363, 369), (90, 90)),
    ((372, 372), (91, 91)),
    ((388, 392), (94, 94)),
    ((394, 394), (96, 96)),
    ((395, 403), (97, 97)),
    ((404, 413), (98, 98)),
    ((414, 420), (99, 99)),
    ((421, 427), (100, 100)),
    ((430, 430), (101, 101)),
    ((446, 450), (106, 106)),
    ((452, 460), (108, 108)),
    ((473, 477), (113, 113)),
    ((479, 479), (115, 115)),
    ((480, 488), (116, 116)),
    ((489, 497), (117, 117)),
    ((510, 514), (122, 122)),
    ((516, 516), (124, 124)),
    ((517, 525), (125, 125)),
    ((526, 534), (126, 126)),
    ((547, 551), (129, 130)),
    ((553, 553), (132, 132)),
    ((554, 562), (133, 133)),
    ((563, 572), (135, 135)),
    ((585, 589), (138, 139)),
    ((591, 591), (141, 141)),
    ((592, 600), (142, 142)),
    ((601, 610), (144, 144)),
    ((623, 627), (147, 147)),
    ((629, 637), (149, 149)),
    ((638, 646), (150, 150)),
    ((647, 655), (151, 151)),
    ((668, 672), (154, 154)),
    ((674, 682), (156, 156)),
    ((683, 690), (157, 157)),
    ((691, 699), (158, 158)),
    ((702, 702), (159, 159)),
    ((718, 722), (162, 162)),
    ((724, 733), (164, 164)),
    ((736, 736), (165, 165)),
    ((752, 756), (168, 168)),
    ((758, 767), (182, 182)),
    ((770, 770), (183, 183)),
    ((786, 790), (186, 186)),
    ((792, 800), (188, 188)),
    ((813, 817), (191, 191)),
    ((819, 828), (193, 193)),
    ((831, 831), (194, 194)),
    ((847, 851), (197, 197)),
    ((853, 862), (202, 202)),
    ((865, 865), (203, 203)),
    ((881, 885), (206, 206)),
    ((887, 894), (208, 208)),
    ((897, 897), (209, 209)),
    ((913, 917), (212, 212)),
    ((919, 928), (214, 214)),
    ((929, 936), (215, 215)),
    ((939, 939), (216, 216)),
    ((943, 943), (217, 217)),
    ((961, 965), (220, 220)),
    ((967, 974), (222, 222)),
    ((975, 984), (223, 223)),
    ((987, 987), (224, 224)),
    ((991, 991), (225, 225)),
)
