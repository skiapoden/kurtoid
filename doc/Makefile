.PHONY: clean all

all: kurtoid.pdf kurtoid.ps kurtoid.txt

kurtoid.pdf: kurtoid.ps
	ps2pdf $^ $@

kurtoid.ps: kurtoid.6
	man -lt $^ > $@

kurtoid.txt: kurtoid.6
	MANWIDTH=72 man -l $^ > $@

clean:
	rm -f kurtoid.pdf kurtoid.ps kurtoid.txt
