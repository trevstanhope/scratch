#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

rec.exe: rec.c
	@echo "This program will fail to compile"
	$(CC) $(CFLAGS) -erec.exe rec.c

clean:
	del rec.exe 
