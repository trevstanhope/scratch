#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

length.exe: length.c
	$(CC) $(CFLAGS) -elength.exe length.c

clean:
	del length.exe 
