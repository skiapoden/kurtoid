.PHONY: clean all

all: kurtoid.pdf kurtoid.ps kurtoid.txt

kurtoid.pdf: kurtoid.ps
	ps2pdf $^ $@

kurtoid.ps: man6/kurtoid.6
	MANPATH=. man -t 6 kurtoid > $@

kurtoid.txt: man6/kurtoid.6
	MANPATH=. MANWIDTH=72 man 6 kurtoid > $@

clean:
	rm -f kurtoid.pdf kurtoid.ps kurtoid.txt
