-module(process1).
-export([main/0, thread/0]).

main()->
    Pid=spawn(process1, thread, []),
    io:fwrite("Spawned new process ~w~n", [Pid]).

thread()->
    io:fwrite("This is a thread.~n", []).
