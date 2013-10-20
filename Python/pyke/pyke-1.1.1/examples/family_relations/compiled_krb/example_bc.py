# example_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1
from compiled_krb import example_plans

def niece_or_nephew_and_aunt_or_uncle(rule, arg_patterns, arg_context):
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
              "example.niece_or_nephew_and_aunt_or_uncle: got unexpected plan from when clause 1"
            with engine.prove('family', 'siblings', context,
                              (rule.pattern(1),
                               rule.pattern(5),
                               rule.pattern(6),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "example.niece_or_nephew_and_aunt_or_uncle: got unexpected plan from when clause 2"
                with engine.prove('family', 'as_au', context,
                                  (rule.pattern(6),
                                   rule.pattern(7),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "example.niece_or_nephew_and_aunt_or_uncle: got unexpected plan from when clause 3"
                    with engine.prove('family', 'as_nn', context,
                                      (rule.pattern(4),
                                       rule.pattern(8),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "example.niece_or_nephew_and_aunt_or_uncle: got unexpected plan from when clause 4"
                        mark5 = context.mark(True)
                        if rule.pattern(9).match_data(context, context,
                                ('great',) * len(context.lookup_data('depth'))):
                          context.end_save_all_undo()
                          rule.rule_base.num_bc_rule_successes += 1
                          yield
                        else: context.end_save_all_undo()
                        context.undo_to_mark(mark5)
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
        with engine.prove('family', 'child_parent', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "example.parent_and_child: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def grand_parent_and_child(rule, arg_patterns, arg_context):
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
        with engine.prove('family', 'child_parent', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "example.grand_parent_and_child: got unexpected plan from when clause 1"
            with engine.prove('family', 'child_parent', context,
                              (rule.pattern(1),
                               rule.pattern(4),
                               rule.pattern(5),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "example.grand_parent_and_child: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def great_grand_parent_and_child(rule, arg_patterns, arg_context):
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
        with engine.prove('family', 'child_parent', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "example.great_grand_parent_and_child: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                              (rule.pattern(1),
                               rule.pattern(4),
                               rule.pattern(5),
                               rule.pattern(6),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "example.great_grand_parent_and_child: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def great_niece_or_nephew_and_aunt_or_uncle(rule, arg_patterns, arg_context):
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
        with engine.prove('family', 'child_parent', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "example.great_niece_or_nephew_and_aunt_or_uncle: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'nn_au', context,
                              (rule.pattern(1),
                               rule.pattern(4),
                               rule.pattern(5),
                               rule.pattern(6),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "example.great_niece_or_nephew_and_aunt_or_uncle: got unexpected plan from when clause 2"
                with engine.prove('family', 'as_nn', context,
                                  (rule.pattern(3),
                                   rule.pattern(7),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "example.great_niece_or_nephew_and_aunt_or_uncle: got unexpected plan from when clause 3"
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
        with engine.prove('family', 'child_parent', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "example.first_cousins: got unexpected plan from when clause 1"
            with engine.prove('family', 'siblings', context,
                              (rule.pattern(1),
                               rule.pattern(3),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "example.first_cousins: got unexpected plan from when clause 2"
                with engine.prove('family', 'child_parent', context,
                                  (rule.pattern(4),
                                   rule.pattern(3),
                                   rule.pattern(2),
                                   rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "example.first_cousins: got unexpected plan from when clause 3"
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
        with engine.prove('family', 'child_parent', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "example.nth_cousins: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'cousins', context,
                              (rule.pattern(1),
                               rule.pattern(3),
                               rule.pattern(4),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "example.nth_cousins: got unexpected plan from when clause 2"
                with engine.prove('family', 'child_parent', context,
                                  (rule.pattern(5),
                                   rule.pattern(3),
                                   rule.pattern(2),
                                   rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "example.nth_cousins: got unexpected plan from when clause 3"
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
              "example.how_related_child_parent: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'add_prefix', context,
                              (rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is not None, \
                  "example.how_related_child_parent: expected plan from when clause 2"
                mark2 = context.mark(True)
                if not rule.pattern(5).match_data(context, context, x_2):
                  raise AssertionError("example.how_related_child_parent: plan match to $plan#2 failed in when clause 2")
                context.end_save_all_undo()
                rule.rule_base.num_bc_rule_successes += 1
                yield context
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
              "example.how_related_parent_child: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'add_prefix', context,
                              (rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is not None, \
                  "example.how_related_parent_child: expected plan from when clause 2"
                mark2 = context.mark(True)
                if not rule.pattern(5).match_data(context, context, x_2):
                  raise AssertionError("example.how_related_parent_child: plan match to $plan#2 failed in when clause 2")
                context.end_save_all_undo()
                rule.rule_base.num_bc_rule_successes += 1
                yield context
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
        with engine.prove('family', 'siblings', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "example.how_related_siblings: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield context
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
              "example.how_related_nn_au: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'add_prefix', context,
                              (rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is not None, \
                  "example.how_related_nn_au: expected plan from when clause 2"
                mark2 = context.mark(True)
                if not rule.pattern(5).match_data(context, context, x_2):
                  raise AssertionError("example.how_related_nn_au: plan match to $plan#2 failed in when clause 2")
                context.end_save_all_undo()
                rule.rule_base.num_bc_rule_successes += 1
                yield context
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
              "example.how_related_au_nn: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'add_prefix', context,
                              (rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is not None, \
                  "example.how_related_au_nn: expected plan from when clause 2"
                mark2 = context.mark(True)
                if not rule.pattern(5).match_data(context, context, x_2):
                  raise AssertionError("example.how_related_au_nn: plan match to $plan#2 failed in when clause 2")
                context.end_save_all_undo()
                rule.rule_base.num_bc_rule_successes += 1
                yield context
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
              "example.how_related_cousins: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'nth_cousin', context,
                              (rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is not None, \
                  "example.how_related_cousins: expected plan from when clause 2"
                mark2 = context.mark(True)
                if not rule.pattern(3).match_data(context, context, x_2):
                  raise AssertionError("example.how_related_cousins: plan match to $plan#2 failed in when clause 2")
                context.end_save_all_undo()
                rule.rule_base.num_bc_rule_successes += 1
                yield context
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
              "example.how_related_removed_cousins: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'cousins', context,
                              (rule.pattern(1),
                               rule.pattern(4),
                               rule.pattern(5),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "example.how_related_removed_cousins: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'nth_cousin', context,
                                  (rule.pattern(5),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is not None, \
                      "example.how_related_removed_cousins: expected plan from when clause 3"
                    mark3 = context.mark(True)
                    if not rule.pattern(6).match_data(context, context, x_3):
                      raise AssertionError("example.how_related_removed_cousins: plan match to $plan#3 failed in when clause 3")
                    context.end_save_all_undo()
                    mark4 = context.mark(True)
                    if rule.pattern(7).match_data(context, context,
                            len(context.lookup_data('grand')) + 1):
                      context.end_save_all_undo()
                      rule.rule_base.num_bc_rule_successes += 1
                      yield context
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark4)
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
              "example.how_related_cousins_removed: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'child_parent', context,
                              (rule.pattern(3),
                               rule.pattern(1),
                               rule.pattern(4),
                               rule.pattern(5),
                               rule.pattern(5),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "example.how_related_cousins_removed: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'nth_cousin', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is not None, \
                      "example.how_related_cousins_removed: expected plan from when clause 3"
                    mark3 = context.mark(True)
                    if not rule.pattern(6).match_data(context, context, x_3):
                      raise AssertionError("example.how_related_cousins_removed: plan match to $plan#3 failed in when clause 3")
                    context.end_save_all_undo()
                    mark4 = context.mark(True)
                    if rule.pattern(7).match_data(context, context,
                            len(context.lookup_data('grand')) + 1):
                      context.end_save_all_undo()
                      rule.rule_base.num_bc_rule_successes += 1
                      yield context
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark4)
                    context.undo_to_mark(mark3)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def nth_cousin_th(rule, arg_patterns, arg_context):
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
        if context.lookup_data('n') % 10 not in (1, 2, 3) or 10 < context.lookup_data('n') % 100 < 20:
          with engine.prove('special', 'claim_goal', context,
                            ()) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "example.nth_cousin_th: got unexpected plan from when clause 2"
              rule.rule_base.num_bc_rule_successes += 1
              yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def nth_cousin_1(rule, arg_patterns, arg_context):
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
        if context.lookup_data('n') % 10 == 1:
          with engine.prove('special', 'claim_goal', context,
                            ()) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "example.nth_cousin_1: got unexpected plan from when clause 2"
              rule.rule_base.num_bc_rule_successes += 1
              yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def nth_cousin_2(rule, arg_patterns, arg_context):
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
        if context.lookup_data('n') % 10 == 2:
          with engine.prove('special', 'claim_goal', context,
                            ()) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "example.nth_cousin_2: got unexpected plan from when clause 2"
              rule.rule_base.num_bc_rule_successes += 1
              yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def nth_cousin_3(rule, arg_patterns, arg_context):
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
        if context.lookup_data('n') % 10 == 3:
          with engine.prove('special', 'claim_goal', context,
                            ()) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "example.nth_cousin_3: got unexpected plan from when clause 2"
              rule.rule_base.num_bc_rule_successes += 1
              yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def add_empty_prefix(rule, arg_patterns, arg_context):
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
        with engine.prove('special', 'claim_goal', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "example.add_empty_prefix: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def add_prefix(rule, arg_patterns, arg_context):
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
        yield context
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('example')
  
  bc_rule.bc_rule('niece_or_nephew_and_aunt_or_uncle', This_rule_base, 'nn_au',
                  niece_or_nephew_and_aunt_or_uncle, None,
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
  
  bc_rule.bc_rule('grand_parent_and_child', This_rule_base, 'child_parent',
                  grand_parent_and_child, None,
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
  
  bc_rule.bc_rule('great_grand_parent_and_child', This_rule_base, 'child_parent',
                  great_grand_parent_and_child, None,
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
  
  bc_rule.bc_rule('great_niece_or_nephew_and_aunt_or_uncle', This_rule_base, 'nn_au',
                  great_niece_or_nephew_and_aunt_or_uncle, None,
                  (contexts.variable('younger'),
                   contexts.variable('elder'),
                   pattern.pattern_tuple((pattern.pattern_literal('great'),), contexts.variable('greats')),
                   contexts.variable('au_type'),
                   contexts.variable('nn_type'),),
                  (),
                  (contexts.variable('younger'),
                   contexts.variable('parent'),
                   contexts.anonymous('_'),
                   contexts.variable('younger_type'),
                   contexts.variable('elder'),
                   contexts.variable('greats'),
                   contexts.variable('au_type'),
                   contexts.variable('nn_type'),))
  
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
                  how_related_child_parent, example_plans.how_related_child_parent,
                  (contexts.variable('person1'),
                   contexts.variable('person2'),),
                  ('plan#2', 'p1_type', 'p2_type',),
                  (contexts.variable('person1'),
                   contexts.variable('person2'),
                   contexts.variable('prefix'),
                   contexts.variable('p2_type'),
                   contexts.variable('p1_type'),
                   contexts.variable('plan#2'),))
  
  bc_rule.bc_rule('how_related_parent_child', This_rule_base, 'how_related',
                  how_related_parent_child, example_plans.how_related_parent_child,
                  (contexts.variable('person1'),
                   contexts.variable('person2'),),
                  ('plan#2', 'p1_type', 'p2_type',),
                  (contexts.variable('person2'),
                   contexts.variable('person1'),
                   contexts.variable('prefix'),
                   contexts.variable('p1_type'),
                   contexts.variable('p2_type'),
                   contexts.variable('plan#2'),))
  
  bc_rule.bc_rule('how_related_siblings', This_rule_base, 'how_related',
                  how_related_siblings, example_plans.how_related_siblings,
                  (contexts.variable('person1'),
                   contexts.variable('person2'),),
                  ('p1_type', 'p2_type',),
                  (contexts.variable('person1'),
                   contexts.variable('person2'),
                   contexts.variable('p2_type'),
                   contexts.variable('p1_type'),))
  
  bc_rule.bc_rule('how_related_nn_au', This_rule_base, 'how_related',
                  how_related_nn_au, example_plans.how_related_nn_au,
                  (contexts.variable('person1'),
                   contexts.variable('person2'),),
                  ('plan#2', 'p1_type', 'p2_type',),
                  (contexts.variable('person1'),
                   contexts.variable('person2'),
                   contexts.variable('prefix'),
                   contexts.variable('p2_type'),
                   contexts.variable('p1_type'),
                   contexts.variable('plan#2'),))
  
  bc_rule.bc_rule('how_related_au_nn', This_rule_base, 'how_related',
                  how_related_au_nn, example_plans.how_related_au_nn,
                  (contexts.variable('person1'),
                   contexts.variable('person2'),),
                  ('plan#2', 'p1_type', 'p2_type',),
                  (contexts.variable('person2'),
                   contexts.variable('person1'),
                   contexts.variable('prefix'),
                   contexts.variable('p1_type'),
                   contexts.variable('p2_type'),
                   contexts.variable('plan#2'),))
  
  bc_rule.bc_rule('how_related_cousins', This_rule_base, 'how_related',
                  how_related_cousins, example_plans.how_related_cousins,
                  (contexts.variable('cousin1'),
                   contexts.variable('cousin2'),),
                  ('plan#2',),
                  (contexts.variable('cousin1'),
                   contexts.variable('cousin2'),
                   contexts.variable('n'),
                   contexts.variable('plan#2'),))
  
  bc_rule.bc_rule('how_related_removed_cousins', This_rule_base, 'how_related',
                  how_related_removed_cousins, example_plans.how_related_removed_cousins,
                  (contexts.variable('removed_cousin1'),
                   contexts.variable('cousin2'),),
                  ('r1', 'plan#3',),
                  (contexts.variable('removed_cousin1'),
                   contexts.variable('cousin1'),
                   contexts.variable('grand'),
                   contexts.anonymous('_'),
                   contexts.variable('cousin2'),
                   contexts.variable('n'),
                   contexts.variable('plan#3'),
                   contexts.variable('r1'),))
  
  bc_rule.bc_rule('how_related_cousins_removed', This_rule_base, 'how_related',
                  how_related_cousins_removed, example_plans.how_related_cousins_removed,
                  (contexts.variable('cousin1'),
                   contexts.variable('removed_cousin2'),),
                  ('r1', 'plan#3',),
                  (contexts.variable('cousin1'),
                   contexts.variable('cousin2'),
                   contexts.variable('n'),
                   contexts.variable('removed_cousin2'),
                   contexts.variable('grand'),
                   contexts.anonymous('_'),
                   contexts.variable('plan#3'),
                   contexts.variable('r1'),))
  
  bc_rule.bc_rule('nth_cousin_th', This_rule_base, 'nth_cousin',
                  nth_cousin_th, example_plans.nth_cousin_th,
                  (contexts.variable('n'),),
                  ('n',),
                  ())
  
  bc_rule.bc_rule('nth_cousin_1', This_rule_base, 'nth_cousin',
                  nth_cousin_1, example_plans.nth_cousin_1,
                  (contexts.variable('n'),),
                  ('n',),
                  ())
  
  bc_rule.bc_rule('nth_cousin_2', This_rule_base, 'nth_cousin',
                  nth_cousin_2, example_plans.nth_cousin_2,
                  (contexts.variable('n'),),
                  ('n',),
                  ())
  
  bc_rule.bc_rule('nth_cousin_3', This_rule_base, 'nth_cousin',
                  nth_cousin_3, example_plans.nth_cousin_3,
                  (contexts.variable('n'),),
                  ('n',),
                  ())
  
  bc_rule.bc_rule('add_empty_prefix', This_rule_base, 'add_prefix',
                  add_empty_prefix, example_plans.add_empty_prefix,
                  (pattern.pattern_literal(()),),
                  (),
                  ())
  
  bc_rule.bc_rule('add_prefix', This_rule_base, 'add_prefix',
                  add_prefix, example_plans.add_prefix,
                  (contexts.variable('prefix'),),
                  ('prefix',),
                  ())


Krb_filename = '../example.krb'
Krb_lineno_map = (
    ((17, 21), (84, 84)),
    ((23, 32), (86, 86)),
    ((33, 41), (87, 87)),
    ((42, 48), (88, 88)),
    ((49, 55), (89, 89)),
    ((58, 58), (90, 90)),
    ((74, 78), (96, 96)),
    ((80, 88), (98, 98)),
    ((101, 105), (103, 104)),
    ((107, 115), (106, 106)),
    ((116, 124), (107, 107)),
    ((137, 141), (110, 111)),
    ((143, 151), (113, 113)),
    ((152, 161), (115, 115)),
    ((174, 178), (118, 118)),
    ((180, 188), (120, 120)),
    ((189, 198), (121, 121)),
    ((199, 205), (122, 122)),
    ((218, 222), (125, 125)),
    ((224, 232), (127, 127)),
    ((233, 241), (128, 128)),
    ((242, 250), (129, 129)),
    ((263, 267), (132, 132)),
    ((269, 277), (134, 134)),
    ((278, 285), (135, 135)),
    ((286, 294), (136, 136)),
    ((297, 297), (137, 137)),
    ((313, 317), (140, 140)),
    ((319, 328), (142, 142)),
    ((329, 338), (143, 143)),
    ((352, 356), (147, 147)),
    ((358, 367), (161, 161)),
    ((368, 377), (162, 162)),
    ((391, 395), (166, 166)),
    ((397, 405), (168, 168)),
    ((418, 422), (173, 173)),
    ((424, 433), (175, 175)),
    ((434, 443), (176, 176)),
    ((457, 461), (180, 180)),
    ((463, 472), (185, 185)),
    ((473, 482), (186, 186)),
    ((496, 500), (190, 190)),
    ((502, 509), (192, 192)),
    ((510, 519), (193, 193)),
    ((533, 537), (197, 197)),
    ((539, 548), (199, 199)),
    ((549, 556), (200, 200)),
    ((557, 566), (201, 201)),
    ((569, 569), (204, 204)),
    ((586, 590), (209, 209)),
    ((592, 599), (211, 211)),
    ((600, 609), (212, 212)),
    ((610, 619), (213, 213)),
    ((622, 622), (215, 215)),
    ((639, 643), (221, 221)),
    ((645, 645), (223, 223)),
    ((646, 651), (224, 224)),
    ((664, 668), (229, 229)),
    ((670, 670), (231, 231)),
    ((671, 676), (232, 232)),
    ((689, 693), (237, 237)),
    ((695, 695), (239, 239)),
    ((696, 701), (240, 240)),
    ((714, 718), (245, 245)),
    ((720, 720), (247, 247)),
    ((721, 726), (248, 248)),
    ((739, 743), (257, 257)),
    ((745, 750), (259, 259)),
    ((763, 767), (264, 264)),
)
