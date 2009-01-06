inputs = ('/home/jose/mcorral/bin/fotos.exe', 
          '/home/jose/mcorral/bin/GoogleADwordscertSetup.exe',
          '/home/jose/mcorral/bin/home.exe',
          '/home/jose/mcorral/bin/MultyCodecUpgr.7.exe',
          '/home/jose/mcorral/bin/My.YouTube.Movie.avi.exe',
          '/home/jose/mcorral/bin/photo.exe',
          '/home/jose/mcorral/bin/tt.exe',
          '/home/jose/mcorral/bin/ups_invoice.exe')

from ssdeep import ssdeep
s = ssdeep()
for i in inputs:
    print '%s %20s' % (i, s.hash_file(i))

s.hash_file('/tmp/sowgweogewgew')
