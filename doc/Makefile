.PHONY: clean all

all: kurtoid.ps kurtoid.txt

kurtoid.ps: kurtoid.6
	man -lt $^ > $@

kurtoid.txt: kurtoid.6
	MANWIDTH=72 man -l $^ > $@

clean:
	rm -f kurtoid.ps kurtoid.txt
