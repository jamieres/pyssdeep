all: ssdeep.c
	python setup.py build

ssdeep.c: ssdeep.pyx
	pyrexc ssdeep.pyx

install: all
	python setup.py install

clean:
	rm -rf ssdeep.c *.so *.o build 

test:
	cp build/lib.linux-i686-2.3/ssdeepmodule.so .
	python test.py

