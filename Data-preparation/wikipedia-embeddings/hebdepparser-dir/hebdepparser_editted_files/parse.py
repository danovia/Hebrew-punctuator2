#!/usr/bin/env python
## Copyright 2010 Yoav Goldberg
##
## This file is part of HebDepParser
##
##    see GPLv3.LICENSE under the main folder for license terms.
##

import copy
import sys
from collections import defaultdict
from itertools import count
from datetime import datetime

import os.path
HERE = os.path.dirname(__file__)
import sys
sys.path.append(os.path.join(HERE,"code","easyfirst"))
import easyfirst
sys.path.append(os.path.join(HERE,"code","labeler"))
import eflabeler
sys.path.append(os.path.join(HERE,"code","preproc"))
import preproc
sys.path.append(os.path.join(HERE,"code","utils"))
import hebtokenizer
sys.path.append(os.path.join(HERE,"tagger"))
import tag

from pio import io
io.ID_TYPE=float
import time

def renumber(sent):
   fmap=defaultdict(count(1).next)
   fmap[0.0]=0
   fmap[-1]=-1
   for t in sent: t['id']=fmap[t['id']]
   for t in sent: t['parent']=fmap[t['parent']]
   for t in sent: t['pparent']=fmap[t['pparent']]


PARSE_MODEL=os.path.join(HERE,"models","hebagr.sp5.model")
LABEL_MODEL=os.path.join(HERE,"models","labeler.f6h.sp5.model.9")

labeler = eflabeler.SimpleSentenceLabeler(eflabeler.Labeler.load(LABEL_MODEL), fext=eflabeler.AnEdgeLabelFeatureExtractor6Heb())
parser = easyfirst.make_parser(PARSE_MODEL, "FINAL")

reader = io.conll_to_sents

def parse_sent(sent, port, OUTSTREAM=sys.stdout, tokenized=False):
   toks = sent.split() if tokenized else [tok for w,tok in hebtokenizer.tokenize(sent)]
   tagged = (unicode(line,"utf8") for line in tag.get_tagged(' '.join(toks), port))
   TEST_SENTS = reader(preproc.yield_conlls(tagged))
   TEST_SENTS = list(TEST_SENTS); assert(len(TEST_SENTS)==1)
   sent = TEST_SENTS[0]
   deps=parser.parse(sent)
   deps.annotate(sent)
   renumber(sent)
   labeler.label(sent, par='pparent',prelout='prel',sent_guides=None)
   io.out_conll(sent,parent='pparent',out=OUTSTREAM)
   return sent

if __name__=='__main__':
   import codecs
   from cStringIO import StringIO
   input = codecs.getreader('utf8')(sys.stdin)
   tokenized='pretok' in sys.argv
   # danzu code:
   i = int(sys.argv[1])
   port = int(sys.argv[2])
   for line in input:
        output = open('./he-morph-new/wiki.he-morph-'+str(i)+'.txt', 'w')
        try:
	        parse_sent(line, port, output, tokenized=tokenized)
		sys.stderr.write(str(datetime.now())+" INFO: Line parsed successfully: "+str(i)+"\n")
	except:
	        sys.stderr.write(str(datetime.now())+" ERROR: Skipped line: "+str(i)+"\n")
	output.close()
	i += 1
