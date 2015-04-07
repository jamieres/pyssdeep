# About #
ssdeep was written by Jesse Kornblum. this is a set of python bindings for it.

the python bindings work with ssdeep 2.0-2.2.

# Example #

```
from ssdeep import ssdeep
s = ssdeep()
# basic hash generation
for i in sys.argv[1:]:
    print '%s %20s' % (i, s.hash_file(i))

h1 = s.hash_file('test.py')
h2 = s.hash_file('setup.py')
print s.compare(h1, h2)
print s.compare(h1, h1)
```

# Requirements #

  1. python 2.x (3.x not tested) - http://www.python.org/
  1. ssdeep - http://ssdeep.sourceforge.net/
  1. pyrex - http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/

# Installation #

  1. get pyssdeep here
  1. unpack ssdeep
  1. unpack pyssdeep under ssdeep (e.g. ssdeep-2.2/pyssdeep )
  1. build ssdeep; install ssdeep; on linux you may have to rerun ldconfig to register libfuzzy
  1. build pyssdeep: make; sudo make install