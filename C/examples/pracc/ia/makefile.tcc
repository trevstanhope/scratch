#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

all:	hist.exe 
 
hist.exe: hist.obj ia.obj ia.h
	$(CC) $(CFLAGS) -ehist hist.obj ia.obj

hist.obj: hist.c ia.h
	$(CC) $(CFLAGS) -c hist.c

ia.obj: ia.c ia.h
	$(CC) $(CFLAGS) -c ia.c

clean:
	del hist.exe hist.obj ia.obj
