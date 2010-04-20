import os
inputs = os.listdir('.')

from ssdeep import ssdeep
s = ssdeep()
hashes = {}
for i in inputs:
    if i.startswith('.'): continue
    h = s.hash_file(i)
    print 'FILE:  %s %20s' % (i, h)
    hashes[i] = h
    if os.path.isdir(i): continue
    f = open(i, 'rb')
    print 'BYTES: %s %20s' % (i, s.hash_bytes(f.read()))
    f.close()

print 'doing comparison'
for k, v in hashes.iteritems():
    for k2, v2 in hashes.iteritems():
        print '%s <-> %s     %d' % (k, k2, s.compare(v, v2))
