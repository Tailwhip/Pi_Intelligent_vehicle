src = $(wildcard *.c)
obj = $(src: .c=.o)

LDFLAGS = -lpthread -lwiringPi -lpigpio -lm
main: $(obj)
	$(CC) -o $@ $^ $(LDFLAGS)

.PHONY: clean
clean:
	rm -f $(obj) main
