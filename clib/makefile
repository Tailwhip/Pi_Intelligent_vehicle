src = $(wildcard *.c)
obj = $(src: .c=.o)

LDFLAGS = -lpthread -lwiringPi -lpigpio 

myprog: $(obj)
	$(CC) -o $@ $^ $(LDFLAGS)

.PHONY: clean
clean:
	rm -f $(obj) myprog
