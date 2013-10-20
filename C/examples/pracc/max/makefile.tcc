#-----------------------------------------------#
#	Makefile for dos systems		#
#    using a Turbo C compiler			#
#-----------------------------------------------#
CC=tcc
CFLAGS=-v -w -ml

max.exe: max.c
	@echo "This program will fail to compile using $(CC)"
	$(CC) $(CFLAGS) -emax.exe max.c

clean:
	del max.exe 
