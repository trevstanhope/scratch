-module(receive1).
-export([main/0,thread/0]).

main()->
    Pid=spawn(receive1,thread,[]),
    io:fwrite("Spawned new process ~w~n", [Pid]),
    Pid ! hello.

thread()->
    io:fwrite("This is a thread.~n", []),
    process_messages().

process_messages()->
    receive
	hello->
	    io:fwrite("Received hello ~n"),
	    process_messages()
		after 2000->
			io:fwrite("Timeout.~n")
			    end.
