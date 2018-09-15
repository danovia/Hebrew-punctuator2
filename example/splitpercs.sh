#!/bin/bash
# usage ./splitpercs.sh file 60 20 20
n=`wc -l <"$1"` || exit 1
echo $* | tr ' ' '\n' | tail -n+2 | head -n`expr $# - 1` |
  awk -v n=$n 'BEGIN{r=1} {r+=n*$0/100; if(r > 1 && r < n){printf "%d\n",r}}' |
  uniq | xargs csplit -sfpart "$1"
