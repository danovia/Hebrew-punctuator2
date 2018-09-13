#!/bin/bash
# downloads hebdeparser and makes needed changes in it
wget https://www.cs.bgu.ac.il/~yoavg/software/hebparsers/hebdepparser/hebdepparser.tgz
tar -xvzf hebdepparser.tgz
cp ./hebdepparser_editted_files/parse.py ./hebdepparser/parse.py
cp ./hebdepparser_editted_files/tagger/tag.py ./hebdepparser/tagger/tag.py
