#!/bin/bash
# split wikipedia to 10 parts for parallel parsing

split -l 20700 wiki.he.text
chmod 755 wiki-text-to-morphemes.sh

mkdir 0
mv xaa 0/
cp wiki-text-to-morphemes.sh 0/

mkdir 1
mv xab 1/
cp wiki-text-to-morphemes.sh 1/

mkdir 2
mv xac 2/
cp wiki-text-to-morphemes.sh 2/

mkdir 3
mv xad 3/
cp wiki-text-to-morphemes.sh 3/

mkdir 4
mv xae 4/
cp wiki-text-to-morphemes.sh 4/

mkdir 5
mv xaf 5/
cp wiki-text-to-morphemes.sh 5/

mkdir 6
mv xag 6/
cp wiki-text-to-morphemes.sh 6/

mkdir 7
mv xah 7/
cp wiki-text-to-morphemes.sh 7/

mkdir 8
mv xai 8/
cp wiki-text-to-morphemes.sh 8/

mkdir 9
mv xaj 9/
cp wiki-text-to-morphemes.sh 9/
