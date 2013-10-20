%%% Recursion, Recursion.erl
%%% Programming Erlang pg. 63
%%% Trevor Stanhope
%% Initials
-module(recursion).
-compile(export_all).

%% Functions
even([])->
    [];
even([Head|Tail]) when Head rem 2 == 0 ->
    [Head | even(Tail)];
even([_|Tail]) ->
    even(Tail).

member(_, []) ->
    false;
member(Head, [Head|_]) ->
    true;
member(Head, [_,Tail]) ->
    member(Head,Tail).

average(List) ->
    average_acc(List,0,0).

average_acc([], Sum, Length)->
    Sum/Length; % when the list is empty, give the sum over the length

average_acc([Head|Tail], Sum, Length) -> % match the head,tail of the list
    average_acc(Tail, Sum + Head, Length + 1). % add the head to the sum counter and increase length
