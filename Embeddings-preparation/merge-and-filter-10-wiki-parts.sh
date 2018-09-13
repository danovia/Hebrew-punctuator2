#!/bin/bash
path="."
# merge wikipedia-dependency-parsed 10 files
start=0
end=9
for ((i=start; i<=end; i++))
do
  echo "Handlling wiki part ${i}"
  files="${path}/${i}/he-morph-new/"
  cd $files
  ls | xargs cat | awk '
    NF {print $2}
    NF==0 {print "|"}
  ' | tr '\n' ' ' | tr '|' '\n' > "wiki-he-morph-${i}.txt"
done

echo "Handlling wiki-FULL"
cat ./wiki-he-morph-*.txt > wiki-he-morph-FULL.txt
