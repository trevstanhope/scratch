#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

PROGS = search1.exe search2.exe search3.exe search4.exe

all: 	$(PROGS) 

search1.exe: search1.c
	$(CC) $(CFLAGS) -esearch1.exe search1.c

search2.exe: search2.c
	$(CC) $(CFLAGS) -esearch2.exe search2.c

search3.exe: search3.c
	$(CC) $(CFLAGS) -esearch3.exe search3.c

search4.exe: search4.c
	$(CC) $(CFLAGS) -esearch4.exe search4.c

clean:
	del search1.exe
	del search2.exe
	del search3.exe
	del search4.exe
