#!/usr/bin/env python
import urllib

INCODE="utf8"
OUTCODE="utf8"

def get_tagged(sent, port):
   params = urllib.urlencode({'text':sent.encode("utf8")})
   #f = urllib.urlopen("http://amdsrv6:8080/bm", params)
   f = urllib.urlopen("http://localhost:"+str(port)+"/bm", params)
   return f.readlines()


if __name__ == '__main__':
   import codecs
   import sys

   fname = sys.argv[1]
   try:
      INCODE = sys.argv[2]
      OUTCODE = sys.argv[3]
   except IndexError: pass
   # assume each line in the file is a sentence
   fh=codecs.open(fname,'r',INCODE)
   for line in fh:
      tagged = get_tagged(line)
      for tok in tagged:
         tok=tok.strip()
         if not tok: continue # this means the tagger split the lines..
         print tok
         #if not tok: continue
         #(w,b,l,c,n) = tok.split()
         #print w.decode("utf8"),b
      print
      #print tagged





