-module(test_fizzbuzz).

-include_lib("eunit/include/eunit.hrl").

analyze_test() ->
    ?assertEqual(1, fizzbuzz:analyze(1)),
    ?assertEqual(fizz, fizzbuzz:analyze(3)).
    
